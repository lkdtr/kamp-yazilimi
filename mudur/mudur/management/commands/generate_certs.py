import logging
import os

from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont
import qrcode

from training.models import Certificate, TrainessCourseRecord
from mudur.models import Site
from training.models import TrainessParticipation

TOTAL_COURSE_HOUR = 66.0
MIN_TIME_TO_GET_CERTIFICATE = 30.0

class Command(BaseCommand):
    help = "Generates the certificate of participation"

    def create_cert_dir(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def generate_cert(self, site, user_profile, course_name, attendance_time):
        camp_year = site.event_start_date.year
        camp_semester = "yaz"
        cert_path = os.getcwd() + "/media/" + str(camp_year) + "/" + str(camp_semester) + "/certs/"
        self.create_cert_dir(cert_path)

        try:
            img = Image.open(os.getcwd() + "/mudur/management/commands/empty_cert.png")
            width, height = img.size
            # Set fonts
            small_font = ImageFont.truetype(os.getcwd() + "/mudur/management/commands/OpenSans-Regular.ttf", 55)
            big_font = ImageFont.truetype(os.getcwd() + "/mudur/management/commands/DancingScript-Regular.ttf", 135)
            signature_font = ImageFont.truetype(os.getcwd() + "/mudur/management/commands/arial.ttf", 35)

            # Prepare the text
            start_date = site.event_start_date.strftime("%d")
            end_date = "31 Ağustos" # site.event_end_date.strftime("%d") + 
            first_sentence = "{start_date} - {end_date} {camp_year} tarihleri arasında Bolu Abant İzzet Baysal Üniversitesi'nde düzenlenen".format(
                start_date=start_date, end_date=end_date, camp_year=camp_year
            )

            camp_semester_label = 'Yaz'

            if camp_semester == "kis":
                camp_semester_label = "Kış"
            else:
                camp_semester_label = "Yaz"

            second_sentence = "Mustafa Akgül Özgür Yazılım {camp_year} {camp_semester_label} Kampı'ndaki ".format(
                camp_year=camp_year, camp_semester_label=camp_semester_label
            ) + '"' + course_name + '"'
            last_sentence = "kursunun {total_course_hour} saatlik programının {attendance_time} saatlik kısmına katılmıştır.".format(
                total_course_hour=TOTAL_COURSE_HOUR,
                attendance_time=attendance_time
            )
            first_name_and_last_name = user_profile.user.first_name.title() + " " + user_profile.user.last_name.title()

            # Write text
            draw = ImageDraw.Draw(img)
            draw.text((width / 2, 1050), first_name_and_last_name.title(), font=big_font, anchor="mm", fill="black")
            draw.text((width / 2, height / 2), first_sentence, font=small_font, anchor="mm", fill="black")
            draw.text((width / 2, height / 2 + 75), second_sentence, font=small_font, anchor="mm", fill="black")
            draw.text((width / 2, height / 2 + 150), last_sentence, font=small_font, anchor="mm", fill="black")

            # Generate and write the signature
            new_cert = Certificate.objects.create(
                user_profile=user_profile, course_name=course_name, camp_year=camp_year, camp_semester=camp_semester
            )
            cert_file_name = new_cert.signature + ".png"
            draw.text(
                (int(width // 2 - 40), height - 40), new_cert.signature, anchor="mm", font=signature_font, fill="black"
            )

            # Generate the QRCode
            qr = qrcode.QRCode(box_size=5)
            qr.add_data(site.home_url + "/media/" + str(camp_year) + "/" + str(camp_semester) + "/certs/" + cert_file_name)
            qr.make()
            img_qr = qr.make_image()
            pos = (img.size[0] - img_qr.size[0] - 80, img.size[1] - img_qr.size[1] - 80)
            img.paste(img_qr, pos)

            # Save the image
            img.save(cert_path + cert_file_name)
            logging.warning("Cert Generated: " + cert_file_name)
        except Exception as err:
            logging.error("User Profile: " + str(user_profile.id) + " Error Occurred: " + str(err))

    def handle(self, *args, **kwargs):
        active_site = Site.objects.get(is_active=True)
        records = TrainessCourseRecord.objects.filter(course__site=active_site, approved=True)
        logging.warning("Total Participation: " + str(records.count()))

        for record in records:
            try:
                user_profile = record.trainess
                morning_sum,afternoon_sum, evening_sum = 0, 0, 0
                tp_instances = TrainessParticipation.objects.filter(courserecord=record)

                for tp in tp_instances:
                    morning_value = 3 if tp.morning == "2" else 0
                    afternoon_value = 3.5 if tp.afternoon == "2" else 0
                    evening_value = 2 if tp.evening == "2" else 0
                    morning_sum += morning_value
                    afternoon_sum += afternoon_value
                    evening_sum += evening_value

                attendance_time = morning_sum + afternoon_sum + evening_sum
                if attendance_time > MIN_TIME_TO_GET_CERTIFICATE:
                    self.generate_cert(active_site, user_profile, record.course.name,  attendance_time)
            except Exception as err:
                logging.error("User Profile: " + str(user_profile.id) + " Error Occurred: " + str(err))
