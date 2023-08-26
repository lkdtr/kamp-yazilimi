from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import mudur.views as mudur_views

admin.autodiscover()
urlpatterns = [
                       url(r'^(?P<menu_id>[1-9]+)/$', mudur_views.index, name="index"),
                       url(r'^$', mudur_views.index, name="index"),
                       url(r'^test', mudur_views.testbeforeapply, name="testbeforeapply"),
                       url(r'^auth/login$', mudur_views.CustomLoginView.as_view(), name="authlogin"),
                       url(r'^auth/logout$', mudur_views.auth_logout, name="authlogout"),
                       url(r'^accounts/', include('userprofile.urls')),
                       url(r'^egitim/', include('training.urls')),
                       url(r'^admin/', include(admin.site.urls), name="admin_entrypoint"),
                       url(r'^survey/', include("surman.urls")),
                       url(r'^ckeditor/', include('ckeditor_uploader.urls')),
                   ]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)