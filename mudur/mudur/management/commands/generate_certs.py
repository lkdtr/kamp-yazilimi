from django.core.management.base import BaseCommand

from mudur.models import Site
from training.models import TrainessCourseRecord

import logging

TOTAL_COURSE_HOUR = 72


class Command(BaseCommand):
    help = 'Generates the certificate of participation'

    def generate_cert(self, site, user_profile, course_name):
        try:
            start_date = site.event_start_date.strftime('%d %B')
            end_date = site.event_end_date.strftime('%d %B')
            camp_year = site.event_start_date.year

            text = "{start_date} - {end_date} tarihleri arasinda Bolu Abant Izzet Baysal Üniversitesi'nde düzenlenen Mustafa " \
                   "Akgül Ozgür Yazilim {camp_year} Yaz Kampi'ndaki {course_name} kursunun {total_course_hour} saatlik programinin {total_course_hour} saatlik kismina katilmistir."
            formatted_text = text.format(total_course_hour=TOTAL_COURSE_HOUR, start_date=start_date, end_date=end_date, camp_year=camp_year, course_name=course_name)
            print(formatted_text)
        except Exception as err:
            logging.error('User Profile: ' + str(user_profile.id) + ' Error Occured: ' + str(err))

    def handle(self, *args, **kwargs):
        active_site = Site.objects.get(is_active=True)
        records = TrainessCourseRecord.objects.filter(course__site=active_site, approved=True)
        logging.warning('Total Participation: ' + str(records.count()))

        for record in records:
            user_profile = record.trainess
            self.generate_cert(active_site, user_profile, record.course.name)