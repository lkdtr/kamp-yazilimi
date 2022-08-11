from django.conf.urls import url

import userprofile.views as userprofile_views

urlpatterns = [
    # register
    url(r"^agreement/$", userprofile_views.accept_agreement, name="accept_agreement"),
    url(r"^kayit", userprofile_views.subscribe, name="subscribe"),
    url(r"^profil", userprofile_views.createprofile, name="createprofile"),
    url(r"^geribildirim", userprofile_views.feedback, name="user_feedback"),
    url(
        r"^getaccomodations/(?P<usertype>[a-zA-Z]+)/(?P<gender>[a-zA-Z]+)",
        userprofile_views.getaccomodations,
        name="getaccomodations",
    ),
    # email verification
    url(r"^active/done/(?P<key>[\w,-]+)/$", userprofile_views.active, name="active"),
    url(r"^active/resend/$", userprofile_views.active_resend, name="active_resend"),
    # for admins
    url(r"^tumkullanicilar", userprofile_views.alluserview, name="alluser"),
    url(r"^tumegitmenler", userprofile_views.get_all_trainers_view, name="alltrainers"),
    # for instructor
    url(r"^egitmen/bilgi", userprofile_views.instructor_information_view, name="instructor_information"),
    url(
        r"^showuser/(?P<userid>[0-9]+)/(?P<courserecordid>[0-9]+)",
        userprofile_views.showuserprofile,
        name="showuserprofile",
    ),
    # password reset
    url(r"^password/reset/$", userprofile_views.password_reset, name="account_reset_password"),
    url(r"^password/reset/key/$", userprofile_views.password_reset_key, name="account_reset_password_key"),
    url(
        r"^password/reset/key/(?P<key>[\w,-]+)/$",
        userprofile_views.password_reset_key_done,
        name="account_reset_password_key_done",
    ),
    url(r"^password/reset/sms/$", userprofile_views.password_reset_by_sms, name="password_reset_by_sms"),
]
