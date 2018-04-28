from django.conf.urls import url
import training.views as training_views

urlpatterns = [
                       url(r'^submit', training_views.submitandregister, name="submit"),
                       url(r'^controlpanel/(?P<courseid>[0-9]+)/$', training_views.control_panel, name="controlpanel"),
                       url(r'^selectcourse/', training_views.select_course_for_control_panel, name="selectcoursefcp"),
                       url(r'^listcourses', training_views.list_courses, name="listcourses"),
                       url(r'^showcourse/(?P<course_id>[0-9]+)/$', training_views.show_course, name="showcourse"),
                       url(r'^applytocourse', training_views.apply_to_course, name="applytocourse"),
                       url(r'^additionprefapply/$', training_views.apply_course_in_addition, name="applytocourseinaddition"),
                       url(r'^basvurular', training_views.allcourseprefview, name="allcoursepref"),
                       url(r'^yoklamalar', training_views.allapprovedprefsview, name="allapprovedprefs"),
                       url(r'^istatistik/$', training_views.statistic, name="statistic"),
                       url(r'^katilimciekle/$', training_views.addtrainess, name="addtrainess"),
                       url(r'^cancelallpreference/$', training_views.cancel_all_preference, name="cancel_all_preference"),
                       # url(r'^cancelcourseapplication/$', 'cancel_course_application', name="cancel_course_application"),  ## 52 numarali issue ile kapatildi
                       url(r'^getpreferredcourses/$', training_views.get_preferred_courses, name="get_preferred_courses"),
                       url(r'^approve_course_preference/$', training_views.approve_course_preference,
                           name="approve_course_preference"),
                       url(r'^participationstatuses/$', training_views.participationstatuses, name='participationstatuses'),
                       url(r'^editparticipationstatus/(?P<courseid>[0-9]+)/(?P<date>[0-9]+)/$', training_views.editparticipationstatusebycourse, name='editparticipationstatusebycourse'),
                       url(r'^printparticipationpages/$', training_views.printparticipationpages, name='printparticipationpages'),
]
