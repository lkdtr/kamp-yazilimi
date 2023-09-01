from PIL import Image, ImageFont, ImageDraw

from django.core.management.base import BaseCommand

from mudur.models import Site
from training.models import TrainessCourseRecord

import logging
import os

TOTAL_COURSE_HOUR = 72


class Command(BaseCommand):
    help = "Generates the certificate of participation"

    def write_text_to_image(self, name, text):
        img = Image.open(os.getcwd() + "/mudur/management/commands/empty_cert.png")
        width, height = img.size
        # Fonts
        small_font = ImageFont.truetype(os.getcwd() + "/mudur/management/commands/arial.ttf", 55)
        big_font = ImageFont.truetype(os.getcwd() + "/mudur/management/commands/arial.ttf", 75)
        # Write texts
        draw = ImageDraw.Draw(img)
        draw.text((width / 2, 1100), name, font=big_font, anchor="mm", fill="black")
        draw.text((width / 2, height / 2), text, font=small_font, anchor="mm", fill="black")

        img.save("created.png")

    def generate_cert(self, site, user_profile, course_name):
        try:
            start_date = site.event_start_date.strftime("%d") + " Ağustos"
            end_date = site.event_end_date.strftime("%d") + " Eylül"
            camp_year = site.event_start_date.year

            text = (
                "{start_date} - {end_date} tarihleri arasında Bolu Abant İzzet Baysal Üniversitesi'nde düzenlenen\n"
                "12. Mustafa Akgül Özgür Yazılım {camp_year} Yaz Kampı'ndaki {course_name}\n"
                "kursunun {total_course_hour} saatlik programının {total_course_hour} saatlık kısmına katılmıştır."
            )
            formatted_text = text.format(
                total_course_hour=TOTAL_COURSE_HOUR,
                start_date=start_date,
                end_date=end_date,
                camp_year=camp_year,
                course_name=course_name,
            )
            print(formatted_text)
            first_name_and_last_name = user_profile.user.first_name.title() + " " + user_profile.user.last_name.title()
            self.write_text_to_image(first_name_and_last_name, formatted_text)
        except Exception as err:
            logging.error("User Profile: " + str(user_profile.id) + " Error Occurred: " + str(err))

    def handle(self, *args, **kwargs):
        active_site = Site.objects.get(is_active=True)
        records = TrainessCourseRecord.objects.filter(course__site=active_site, approved=True)
        logging.warning("Total Participation: " + str(records.count()))

        for record in records:
            user_profile = record.trainess
            self.generate_cert(active_site, user_profile, record.course.name)
