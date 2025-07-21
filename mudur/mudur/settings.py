"""
Django settings for mudur project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

"""
    DJANGO_ROOT: Django kodlarının bulunduğu dizin
    PROJECT_ROOT: Git reposunun bulunduğu yer
    VIRTUAL_ENV_PATH: Uygulamanın virtualenv'nin kurulu oldugu dizinin yolu, VIRTUAL_ENV ortam değişkeninden alır
"""
DJANGO_ROOT = BASE_DIR
PROJECT_ROOT = os.path.dirname(DJANGO_ROOT)
VIRTUAL_ENV_PATH = os.getenv("VIRTUAL_ENV", os.path.join(PROJECT_ROOT, "venv"))

sys.path.insert(0, os.path.join(BASE_DIR, "mudur"))

"""
    MUDUR_CONFIG: Veri tabani ayarlari ve secret key bu dosyada yer alir.
"""


def validate_mudur_config(setting):
    import configparser as ConfigParser

    if MUDUR_CONFIG is None:
        raise ValueError("MUDUR_CONFIG is not defined")
    elif not os.path.exists(setting):
        raise ValueError("MUDUR_CONFIG do not exist")
    elif not setting:
        raise ValueError("MUDUR_CONFIG do not exist")
    config = ConfigParser.ConfigParser()
    config.read(setting)


MUDUR_CONFIG = os.getenv("MUDUR_CONFIG", None)
validate_mudur_config(MUDUR_CONFIG)

from .readconf import *

"""
    EMAIL_FROM_ADDRESS: Sistemden gonderilecek maillerin from adresi
"""
emailsettings = EmailSettings()
EMAIL_FROM_ADDRESS = emailsettings.fromaddress
EMAIL_HOST = emailsettings.host
EMAIL_HOST_USER = emailsettings.username
EMAIL_HOST_PASSWORD = emailsettings.password
EMAIL_PORT = emailsettings.port

SEND_REPORT = True
REPORT_RECIPIENT_LIST = ["kamp-gelismeler@linux.org.tr"]

"""
    PREFERENCE_LIMIT: Kurs tercih limiti
"""
PREFERENCE_LIMIT = 3

"""
    ADDITION_PREFERENCE_LIMIT: Ek kurs tercih limiti
"""
ADDITION_PREFERENCE_LIMIT = 1

"""
    ACCOMODATION_PREFERENCE_LIMIT: Konaklama tercih limiti
"""
ACCOMODATION_PREFERENCE_LIMIT = 1

"""
    USER_TYPES: Sistemden olusturulacak kullanicilarin turleri
"""
USER_TYPES = {"inst": "instructor", "stu": "student", "hepsi": "hepsi"}

"""
    TRAINESS_PARTICIPATION_STATE: Kursiyerin kursa katilip katilmadigi
"""
TRAINESS_PARTICIPATION_STATE = [
    ("-1", "Kurs Yapılmadı"),
    ("0", "Katılmadı"),
    ("1", "Yarısına Katıldı"),
    ("2", "Katıldı"),
]

"""
   GENDER: Profilde kullaniliyor
"""
GENDER = {"E": "Erkek", "K": "Kadin", "H": "Hepsi"}

"""
   TRANSPORTATION: Egitmenin ulasim sekli
"""
TRANSPORTATION = {"0": "Uçak", "1": "Otobüs", "2": "Araba", "3": "Diğer"}

CITIES_LIGHT_TRANSLATION_LANGUAGES = ["tr", "en"]
CITIES_LIGHT_INCLUDE_COUNTRIES = ["TR"]
CITIES_LIGHT_INCLUDE_CITY_TYPES = ["ADM1", "ADM2"]

CKEDITOR_UPLOAD_PATH = "/static/"
CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"

"""
   TC Kimlik numarasını dogrularken kullanilan web servis
"""
TCKIMLIK_SORGULAMA_WS = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?WSDL"
"""
   REQUIRE_TRAINESS_APPROVE: Akademik Bilisimde katilimci kursa kabul edildikten sonra yeniden katılıp katılmayacağına
                            dair teyit alıyoruz. (True)
                            Kamp'ta öyle bir durum yok.(False)
"""
REQUIRE_TRAINESS_APPROVE = False


MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
DJANGOSETTINGS = DjangoSettings()
SECRET_KEY = DJANGOSETTINGS.getsecretkey()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("MUDUR_DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = ["*"]

# Application definition
REQUIRE_UNIQUE_EMAIL = False

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.views",
    "mudur",
    "userprofile",
    "training",
    "ckeditor",
    "ckeditor_uploader",
    "django_countries",
    "mailing",
    "surman",
    "cities_light",
    "bootstrap3",
    "django_extensions",
    "captcha",
)

captchasettings = CaptchaSettings()
RECAPTCHA_PUBLIC_KEY = captchasettings.get_public_key()
RECAPTCHA_PRIVATE_KEY = captchasettings.get_private_key()
NOCAPTCHA = True

MIDDLEWARE_CLASSES = (
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "mudur.middleware.extra.LogVariablesMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "mudur.middleware.site.CurrentSiteMiddleware",
    "mudur.middleware.agreement.AgreementMiddleware",
)
ROOT_URLCONF = "mudur.urls"
CSRF_COOKIE_SECURE = os.getenv("MUDUR_HTTPS", "false").lower() == "true"
SESSION_COOKIE_SECURE = os.getenv("MUDUR_HTTPS", "false").lower() == "true"
X_FRAME_OPTIONS = "DENY"
WSGI_APPLICATION = "mudur.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DBCONF = DBconfig()

LOGIN_REDIRECT_URL = "/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DBCONF.getdatabase(),
        "USER": DBCONF.getdbuser(),
        "PASSWORD": DBCONF.getdbpass(),
        "HOST": DBCONF.getdbhost(),
        "PORT": DBCONF.getdbport(),
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale/"),)

LANGUAGE_CODE = "tr"

# TIME_ZONE = 'GMT'
# TIME_ZONE = 'Europe/Istanbul'
TIME_ZONE = "Asia/Baghdad"

USE_I18N = True

USE_L10N = True

USE_TZ = False
DATE_FORMAT = "dMY"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates/")],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "mudur.context_processors.menu",
            ],
        },
    },
]

LOGIN_URL = "/"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] [%(clientip)s - %(user)-8s] %(levelname)s [%(name)s:%(lineno)s]  %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s]  %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "logfile": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR + "/logfile",
            "maxBytes": 2097152,
            "backupCount": 200,
            "formatter": "standard",
        },
        "console": {"level": "INFO", "class": "logging.StreamHandler", "formatter": "simple"},
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": True,
            "level": "WARN",
        },
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "mudur": {
            "handlers": ["logfile"],
            "level": "DEBUG",
        },
        "userprofile": {
            "handlers": ["logfile"],
            "level": "DEBUG",
        },
        "seminar": {
            "handlers": ["logfile"],
            "level": "DEBUG",
        },
        "training": {
            "handlers": ["logfile"],
            "level": "DEBUG",
        },
    },
}

sms_settings = SMSSettings()
SMS_URL = sms_settings.get_url()
SMS_USERCODE = sms_settings.get_usercode()
SMS_PASSWORD = sms_settings.get_password()
SMS_MSGHEADER = sms_settings.get_msgheader()

UNIVERSITIES = [
    ("Abdullah Gül Üniversitesi (Kayseri)", "Abdullah Gül Üniversitesi (Kayseri)"),
    ("Acıbadem Mehmet Ali Aydınlar Üniversitesi (İstanbul)", "Acıbadem Mehmet Ali Aydınlar Üniversitesi (İstanbul)"),
    ("Adana Alparslan Türkeş Bilim Ve Teknoloji Üniversitesi (Adana)", "Adana Alparslan Türkeş Bilim Ve Teknoloji Üniversitesi (Adana)"),
    ("Adıyaman Üniversitesi (Adıyaman)", "Adıyaman Üniversitesi (Adıyaman)"),
    ("Afyon Kocatepe Üniversitesi (Afyon)", "Afyon Kocatepe Üniversitesi (Afyon)"),
    ("Afyonkarahisar Sağlık Bilimleri Üniversitesi (Afyon)", "Afyonkarahisar Sağlık Bilimleri Üniversitesi (Afyon)"),
    ("Ağrı İbrahim Çeçen Üniversitesi (Ağrı)", "Ağrı İbrahim Çeçen Üniversitesi (Ağrı)"),
    ("Akdeniz Üniversitesi (Antalya)", "Akdeniz Üniversitesi (Antalya)"),
    ("Aksaray Üniversitesi (Aksaray)", "Aksaray Üniversitesi (Aksaray)"),
    ("Alanya Alaaddin Keykubat Üniversitesi (Antalya)", "Alanya Alaaddin Keykubat Üniversitesi (Antalya)"),
    ("Alanya Üniversitesi (Antalya)", "Alanya Üniversitesi (Antalya)"),
    ("Altınbaş Üniversitesi (İstanbul)", "Altınbaş Üniversitesi (İstanbul)"),
    ("Amasya Üniversitesi (Amasya)", "Amasya Üniversitesi (Amasya)"),
    ("Anadolu Üniversitesi (Eskişehir)", "Anadolu Üniversitesi (Eskişehir)"),
    ("Ankara Bilim Üniversitesi (Ankara)", "Ankara Bilim Üniversitesi (Ankara)"),
    ("Ankara Hacı Bayram Veli Üniversitesi (Ankara)", "Ankara Hacı Bayram Veli Üniversitesi (Ankara)"),
    ("Ankara Medipol Üniversitesi (Ankara)", "Ankara Medipol Üniversitesi (Ankara)"),
    ("Ankara Müzik Ve Güzel Sanatlar Üniversitesi (Ankara)", "Ankara Müzik Ve Güzel Sanatlar Üniversitesi (Ankara)"),
    ("Ankara Sosyal Bilimler Üniversitesi (Ankara)", "Ankara Sosyal Bilimler Üniversitesi (Ankara)"),
    ("Ankara Üniversitesi (Ankara)", "Ankara Üniversitesi (Ankara)"),
    ("Ankara Yıldırım Beyazıt Üniversitesi (Ankara)", "Ankara Yıldırım Beyazıt Üniversitesi (Ankara)"),
    ("Antalya Belek Üniversitesi (Antalya)", "Antalya Belek Üniversitesi (Antalya)"),
    ("Antalya Bilim Üniversitesi (Antalya)", "Antalya Bilim Üniversitesi (Antalya)"),
    ("Ardahan Üniversitesi (Ardahan)", "Ardahan Üniversitesi (Ardahan)"),
    ("Artvin Çoruh Üniversitesi (Artvin)", "Artvin Çoruh Üniversitesi (Artvin)"),
    ("Ataşehir Adıgüzel Meslek Yüksekokulu (İstanbul)", "Ataşehir Adıgüzel Meslek Yüksekokulu (İstanbul)"),
    ("Atatürk Üniversitesi (Erzurum)", "Atatürk Üniversitesi (Erzurum)"),
    ("Atılım Üniversitesi (Ankara)", "Atılım Üniversitesi (Ankara)"),
    ("Avrasya Üniversitesi (Trabzon)", "Avrasya Üniversitesi (Trabzon)"),
    ("Aydın Adnan Menderes Üniversitesi (Aydın)", "Aydın Adnan Menderes Üniversitesi (Aydın)"),
    ("Bahçeşehir Üniversitesi (İstanbul)", "Bahçeşehir Üniversitesi (İstanbul)"),
    ("Balıkesir Üniversitesi (Balıkesir)", "Balıkesir Üniversitesi (Balıkesir)"),
    ("Bandırma Onyedi Eylül Üniversitesi (Balıkesir)", "Bandırma Onyedi Eylül Üniversitesi (Balıkesir)"),
    ("Bartın Üniversitesi (Bartın)", "Bartın Üniversitesi (Bartın)"),
    ("Başkent Üniversitesi (Ankara)", "Başkent Üniversitesi (Ankara)"),
    ("Batman Üniversitesi (Batman)", "Batman Üniversitesi (Batman)"),
    ("Bayburt Üniversitesi (Bayburt)", "Bayburt Üniversitesi (Bayburt)"),
    ("Beykoz Üniversitesi (İstanbul)", "Beykoz Üniversitesi (İstanbul)"),
    ("Bezm-İ Âlem Vakıf Üniversitesi (İstanbul)", "Bezm-İ Âlem Vakıf Üniversitesi (İstanbul)"),
    ("Bilecik Şeyh Edebali Üniversitesi (Bilecik)", "Bilecik Şeyh Edebali Üniversitesi (Bilecik)"),
    ("Bingöl Üniversitesi (Bingöl)", "Bingöl Üniversitesi (Bingöl)"),
    ("Biruni Üniversitesi (İstanbul)", "Biruni Üniversitesi (İstanbul)"),
    ("Bitlis Eren Üniversitesi (Bitlis)", "Bitlis Eren Üniversitesi (Bitlis)"),
    ("Boğaziçi Üniversitesi (İstanbul)", "Boğaziçi Üniversitesi (İstanbul)"),
    ("Bolu Abant İzzet Baysal Üniversitesi (Bolu)", "Bolu Abant İzzet Baysal Üniversitesi (Bolu)"),
    ("Burdur Mehmet Akif Ersoy Üniversitesi (Burdur)", "Burdur Mehmet Akif Ersoy Üniversitesi (Burdur)"),
    ("Bursa Teknik Üniversitesi (Bursa)", "Bursa Teknik Üniversitesi (Bursa)"),
    ("Bursa Uludağ Üniversitesi (Bursa)", "Bursa Uludağ Üniversitesi (Bursa)"),
    ("Çağ Üniversitesi (Mersin)", "Çağ Üniversitesi (Mersin)"),
    ("Çanakkale Onsekiz Mart Üniversitesi (Çanakkale)", "Çanakkale Onsekiz Mart Üniversitesi (Çanakkale)"),
    ("Çankaya Üniversitesi (Ankara)", "Çankaya Üniversitesi (Ankara)"),
    ("Çankırı Karatekin Üniversitesi (Çankırı)", "Çankırı Karatekin Üniversitesi (Çankırı)"),
    ("Çukurova Üniversitesi (Adana)", "Çukurova Üniversitesi (Adana)"),
    ("Demiroğlu Bilim Üniversitesi (İstanbul)", "Demiroğlu Bilim Üniversitesi (İstanbul)"),
    ("Dicle Üniversitesi (Diyarbakır)", "Dicle Üniversitesi (Diyarbakır)"),
    ("Doğuş Üniversitesi (İstanbul)", "Doğuş Üniversitesi (İstanbul)"),
    ("Dokuz Eylül Üniversitesi (İzmir)", "Dokuz Eylül Üniversitesi (İzmir)"),
    ("Düzce Üniversitesi (Düzce)", "Düzce Üniversitesi (Düzce)"),
    ("Ege Üniversitesi (İzmir)", "Ege Üniversitesi (İzmir)"),
    ("Erciyes Üniversitesi (Kayseri)", "Erciyes Üniversitesi (Kayseri)"),
    ("Erzincan Binali Yıldırım Üniversitesi (Erincan)", "Erzincan Binali Yıldırım Üniversitesi (Erincan)"),
    ("Erzurum Teknik Üniversitesi (Erzurum)", "Erzurum Teknik Üniversitesi (Erzurum)"),
    ("Eskişehir Osmangazi Üniversitesi (Eskişehir)", "Eskişehir Osmangazi Üniversitesi (Eskişehir)"),
    ("Eskişehir Teknik Üniversitesi (Eskişehir)", "Eskişehir Teknik Üniversitesi (Eskişehir)"),
    ("Fatih Sultan Mehmet Vakıf Üniversitesi (İstanbul)", "Fatih Sultan Mehmet Vakıf Üniversitesi (İstanbul)"),
    ("Fenerbahçe Üniversitesi (İstanbul)", "Fenerbahçe Üniversitesi (İstanbul)"),
    ("Fırat Üniversitesi (Elazığ)", "Fırat Üniversitesi (Elazığ)"),
    ("Galatasaray Üniversitesi (İstanbul)", "Galatasaray Üniversitesi (İstanbul)"),
    ("Gazi Üniversitesi (Ankara)", "Gazi Üniversitesi (Ankara)"),
    ("Gaziantep İslam Bilim Ve Teknoloji Üniversitesi (Gaziantep)", "Gaziantep İslam Bilim Ve Teknoloji Üniversitesi (Gaziantep)"),
    ("Gaziantep Üniversitesi (Gaziantep)", "Gaziantep Üniversitesi (Gaziantep)"),
    ("Gebze Teknik Üniversitesi (Kocaeli)", "Gebze Teknik Üniversitesi (Kocaeli)"),
    ("Giresun Üniversitesi (Giresun)", "Giresun Üniversitesi (Giresun)"),
    ("Gümüşhane Üniversitesi (Gümüşhane)", "Gümüşhane Üniversitesi (Gümüşhane)"),
    ("Hacettepe Üniversitesi (Ankara)", "Hacettepe Üniversitesi (Ankara)"),
    ("Hakkari Üniversitesi (Hakkari)", "Hakkari Üniversitesi (Hakkari)"),
    ("Haliç Üniversitesi (İstanbul)", "Haliç Üniversitesi (İstanbul)"),
    ("Harran Üniversitesi (Şanlıurfa)", "Harran Üniversitesi (Şanlıurfa)"),
    ("Hasan Kalyoncu Üniversitesi (Gaziantep)", "Hasan Kalyoncu Üniversitesi (Gaziantep)"),
    ("Hatay Mustafa Kemal Üniversitesi (Hatay)", "Hatay Mustafa Kemal Üniversitesi (Hatay)"),
    ("Hitit Üniversitesi (Çorum)", "Hitit Üniversitesi (Çorum)"),
    ("Iğdır Üniversitesi (Iğdır)", "Iğdır Üniversitesi (Iğdır)"),
    ("Isparta Uygulamalı Bilimler Üniversitesi (Isparta)", "Isparta Uygulamalı Bilimler Üniversitesi (Isparta)"),
    ("Işık Üniversitesi (İstanbul)", "Işık Üniversitesi (İstanbul)"),
    ("İbn Haldun Üniversitesi (İstanbul)", "İbn Haldun Üniversitesi (İstanbul)"),
    ("İhsan Doğramacı Bilkent Üniversitesi (Ankara)", "İhsan Doğramacı Bilkent Üniversitesi (Ankara)"),
    ("İnönü Üniversitesi (Malatya)", "İnönü Üniversitesi (Malatya)"),
    ("İskenderun Teknik Üniversitesi (Hatay)", "İskenderun Teknik Üniversitesi (Hatay)"),
    ("İstanbul Arel Üniversitesi (İstanbul)", "İstanbul Arel Üniversitesi (İstanbul)"),
    ("İstanbul Atlas Üniversitesi (İstanbul)", "İstanbul Atlas Üniversitesi (İstanbul)"),
    ("İstanbul Aydın Üniversitesi (İstanbul)", "İstanbul Aydın Üniversitesi (İstanbul)"),
    ("İstanbul Beykent Üniversitesi (İstanbul)", "İstanbul Beykent Üniversitesi (İstanbul)"),
    ("İstanbul Bilgi Üniversitesi (İstanbul)", "İstanbul Bilgi Üniversitesi (İstanbul)"),
    ("İstanbul Esenyurt Üniversitesi (İstanbul)", "İstanbul Esenyurt Üniversitesi (İstanbul)"),
    ("İstanbul Galata Üniversitesi (İstanbul)", "İstanbul Galata Üniversitesi (İstanbul)"),
    ("İstanbul Gedik Üniversitesi (İstanbul)", "İstanbul Gedik Üniversitesi (İstanbul)"),
    ("İstanbul Gelişim Üniversitesi (İstanbul)", "İstanbul Gelişim Üniversitesi (İstanbul)"),
    ("İstanbul Kent Üniversitesi (İstanbul)", "İstanbul Kent Üniversitesi (İstanbul)"),
    ("İstanbul Kültür Üniversitesi (İstanbul)", "İstanbul Kültür Üniversitesi (İstanbul)"),
    ("İstanbul Medeniyet Üniversitesi (İstanbul)", "İstanbul Medeniyet Üniversitesi (İstanbul)"),
    ("İstanbul Medipol Üniversitesi (İstanbul)", "İstanbul Medipol Üniversitesi (İstanbul)"),
    ("İstanbul Nişantaşı Üniversitesi (İstanbul)", "İstanbul Nişantaşı Üniversitesi (İstanbul)"),
    ("İstanbul Okan Üniversitesi (İstanbul)", "İstanbul Okan Üniversitesi (İstanbul)"),
    ("İstanbul Rumeli Üniversitesi (İstanbul)", "İstanbul Rumeli Üniversitesi (İstanbul)"),
    ("İstanbul Sabahattin Zaim Üniversitesi (İstanbul)", "İstanbul Sabahattin Zaim Üniversitesi (İstanbul)"),
    ("İstanbul Sağlık Ve Sosyal Bilimler Meslek Yüksekokulu (İstanbul)", "İstanbul Sağlık Ve Sosyal Bilimler Meslek Yüksekokulu (İstanbul)"),
    ("İstanbul Sağlık Ve Teknoloji Üniversitesi (İstanbul)", "İstanbul Sağlık Ve Teknoloji Üniversitesi (İstanbul)"),
    ("İstanbul Şişli Meslek Yüksekokulu (İstanbul)", "İstanbul Şişli Meslek Yüksekokulu (İstanbul)"),
    ("İstanbul Teknik Üniversitesi (İstanbul)", "İstanbul Teknik Üniversitesi (İstanbul)"),
    ("İstanbul Ticaret Üniversitesi (İstanbul)", "İstanbul Ticaret Üniversitesi (İstanbul)"),
    ("İstanbul Topkapı Üniversitesi (İstanbul)", "İstanbul Topkapı Üniversitesi (İstanbul)"),
    ("İstanbul Üniversitesi (İstanbul)", "İstanbul Üniversitesi (İstanbul)"),
    ("İstanbul Üniversitesi-Cerrahpaşa (İstanbul)", "İstanbul Üniversitesi-Cerrahpaşa (İstanbul)"),
    ("İstanbul Yeni Yüzyıl Üniversitesi (İstanbul)", "İstanbul Yeni Yüzyıl Üniversitesi (İstanbul)"),
    ("İstanbul 29 Mayıs Üniversitesi (İstanbul)", "İstanbul 29 Mayıs Üniversitesi (İstanbul)"),
    ("İstinye Üniversitesi (İstanbul)", "İstinye Üniversitesi (İstanbul)"),
    ("İzmir Bakırçay Üniversitesi (İzmir)", "İzmir Bakırçay Üniversitesi (İzmir)"),
    ("İzmir Demokrasi Üniversitesi (İzmir)", "İzmir Demokrasi Üniversitesi (İzmir)"),
    ("İzmir Ekonomi Üniversitesi (İzmir)", "İzmir Ekonomi Üniversitesi (İzmir)"),
    ("İzmir Katip Çelebi Üniversitesi (İzmir)", "İzmir Katip Çelebi Üniversitesi (İzmir)"),
    ("İzmir Kavram Meslek Yüksekokulu (İzmir)", "İzmir Kavram Meslek Yüksekokulu (İzmir)"),
    ("İzmir Tınaztepe Üniversitesi (İzmir)", "İzmir Tınaztepe Üniversitesi (İzmir)"),
    ("İzmir Yüksek Teknoloji Enstitüsü (İzmir)", "İzmir Yüksek Teknoloji Enstitüsü (İzmir)"),
    ("Kadir Has Üniversitesi (İstanbul)", "Kadir Has Üniversitesi (İstanbul)"),
    ("Kafkas Üniversitesi (Kars)", "Kafkas Üniversitesi (Kars)"),
    ("Kahramanmaraş İstiklal Üniversitesi (Kahramanmaraş)", "Kahramanmaraş İstiklal Üniversitesi (Kahramanmaraş)"),
    ("Kahramanmaraş Sütçü İmam Üniversitesi (Kahramanmaraş)", "Kahramanmaraş Sütçü İmam Üniversitesi (Kahramanmaraş)"),
    ("Kapadokya Üniversitesi (Nevşehir)", "Kapadokya Üniversitesi (Nevşehir)"),
    ("Karabük Üniversitesi (Karabük)", "Karabük Üniversitesi (Karabük)"),
    ("Karadeniz Teknik Üniversitesi (Trabzon)", "Karadeniz Teknik Üniversitesi (Trabzon)"),
    ("Karamanoğlu Mehmetbey Üniversitesi (Karaman)", "Karamanoğlu Mehmetbey Üniversitesi (Karaman)"),
    ("Kastamonu Üniversitesi (Kastamonu)", "Kastamonu Üniversitesi (Kastamonu)"),
    ("Kayseri Üniversitesi (Kayseri)", "Kayseri Üniversitesi (Kayseri)"),
    ("Kırıkkale Üniversitesi (Kırıkkale)", "Kırıkkale Üniversitesi (Kırıkkale)"),
    ("Kırklareli Üniversitesi (Kırklareli)", "Kırklareli Üniversitesi (Kırklareli)"),
    ("Kırşehir Ahi Evran Üniversitesi (Kırşehir)", "Kırşehir Ahi Evran Üniversitesi (Kırşehir)"),
    ("Kilis 7 Aralık Üniversitesi (Kilis)", "Kilis 7 Aralık Üniversitesi (Kilis)"),
    ("Kocaeli Sağlık Ve Teknoloji Üniversitesi (Kocaeli)", "Kocaeli Sağlık Ve Teknoloji Üniversitesi (Kocaeli)"),
    ("Kocaeli Üniversitesi (Kocaeli)", "Kocaeli Üniversitesi (Kocaeli)"),
    ("Koç Üniversitesi (İstanbul)", "Koç Üniversitesi (İstanbul)"),
    ("Konya Gıda Ve Tarım Üniversitesi (Konya)", "Konya Gıda Ve Tarım Üniversitesi (Konya)"),
    ("Konya Teknik Üniversitesi (Konya)", "Konya Teknik Üniversitesi (Konya)"),
    ("Kto Karatay Üniversitesi (Konya)", "Kto Karatay Üniversitesi (Konya)"),
    ("Kütahya Dumlupınar Üniversitesi (Kütahya)", "Kütahya Dumlupınar Üniversitesi (Kütahya)"),
    ("Kütahya Sağlık Bilimleri Üniversitesi (Kütahya)", "Kütahya Sağlık Bilimleri Üniversitesi (Kütahya)"),
    ("Lokman Hekim Üniversitesi (Ankara)", "Lokman Hekim Üniversitesi (Ankara)"),
    ("Malatya Turgut Özal Üniversitesi (Malatya)", "Malatya Turgut Özal Üniversitesi (Malatya)"),
    ("Maltepe Üniversitesi (İstanbul)", "Maltepe Üniversitesi (İstanbul)"),
    ("Manisa Celâl Bayar Üniversitesi (Manisa)", "Manisa Celâl Bayar Üniversitesi (Manisa)"),
    ("Mardin Artuklu Üniversitesi (Mardin)", "Mardin Artuklu Üniversitesi (Mardin)"),
    ("Marmara Üniversitesi (İstanbul)", "Marmara Üniversitesi (İstanbul)"),
    ("Mef Üniversitesi (İstanbul)", "Mef Üniversitesi (İstanbul)"),
    ("Mersin Üniversitesi (Mersin)", "Mersin Üniversitesi (Mersin)"),
    ("Mimar Sinan Güzel Sanatlar Üniversitesi (İstanbul)", "Mimar Sinan Güzel Sanatlar Üniversitesi (İstanbul)"),
    ("Mudanya Üniversitesi (Bursa)", "Mudanya Üniversitesi (Bursa)"),
    ("Muğla Sıtkı Koçman Üniversitesi (Muğla)", "Muğla Sıtkı Koçman Üniversitesi (Muğla)"),
    ("Munzur Üniversitesi (Tunceli)", "Munzur Üniversitesi (Tunceli)"),
    ("Muş Alparslan Üniversitesi (Muş)", "Muş Alparslan Üniversitesi (Muş)"),
    ("Necmettin Erbakan Üniversitesi (Konya)", "Necmettin Erbakan Üniversitesi (Konya)"),
    ("Nevşehir Hacı Bektaş Veli Üniversitesi (Nevşehir)", "Nevşehir Hacı Bektaş Veli Üniversitesi (Nevşehir)"),
    ("Niğde Ömer Halisdemir Üniversitesi (Niğde)", "Niğde Ömer Halisdemir Üniversitesi (Niğde)"),
    ("Nuh Naci Yazgan Üniversitesi (Kayseri)", "Nuh Naci Yazgan Üniversitesi (Kayseri)"),
    ("Ondokuz Mayıs Üniversitesi (Samsun)", "Ondokuz Mayıs Üniversitesi (Samsun)"),
    ("Ordu Üniversitesi (Ordu)", "Ordu Üniversitesi (Ordu)"),
    ("Orta Doğu Teknik Üniversitesi (Ankara)", "Orta Doğu Teknik Üniversitesi (Ankara)"),
    ("Osmaniye Korkut Ata Üniversitesi (Osmaniye)", "Osmaniye Korkut Ata Üniversitesi (Osmaniye)"),
    ("Ostim Teknik Üniversitesi (Ankara)", "Ostim Teknik Üniversitesi (Ankara)"),
    ("Özyeğin Üniversitesi (İstanbul)", "Özyeğin Üniversitesi (İstanbul)"),
    ("Pamukkale Üniversitesi (Denizli)", "Pamukkale Üniversitesi (Denizli)"),
    ("Piri Reis Üniversitesi (İstanbul)", "Piri Reis Üniversitesi (İstanbul)"),
    ("Recep Tayyip Erdoğan Üniversitesi (Rize)", "Recep Tayyip Erdoğan Üniversitesi (Rize)"),
    ("Sabancı Üniversitesi (İstanbul)", "Sabancı Üniversitesi (İstanbul)"),
    ("Sağlık Bilimleri Üniversitesi (İstanbul)", "Sağlık Bilimleri Üniversitesi (İstanbul)"),
    ("Sakarya Uygulamalı Bilimler Üniversitesi (Sakarya)", "Sakarya Uygulamalı Bilimler Üniversitesi (Sakarya)"),
    ("Sakarya Üniversitesi (Sakarya)", "Sakarya Üniversitesi (Sakarya)"),
    ("Samsun Üniversitesi (Samsun)", "Samsun Üniversitesi (Samsun)"),
    ("Sanko Üniversitesi (Gaziantep)", "Sanko Üniversitesi (Gaziantep)"),
    ("Selçuk Üniversitesi (Konya)", "Selçuk Üniversitesi (Konya)"),
    ("Siirt Üniversitesi (Siirt)", "Siirt Üniversitesi (Siirt)"),
    ("Sinop Üniversitesi (Sinop)", "Sinop Üniversitesi (Sinop)"),
    ("Sivas Bilim Ve Teknoloji Üniversitesi (Sivas)", "Sivas Bilim Ve Teknoloji Üniversitesi (Sivas)"),
    ("Sivas Cumhuriyet Üniversitesi (Sivas)", "Sivas Cumhuriyet Üniversitesi (Sivas)"),
    ("Süleyman Demirel Üniversitesi (Isparta)", "Süleyman Demirel Üniversitesi (Isparta)"),
    ("Şırnak Üniversitesi (Şırnak)", "Şırnak Üniversitesi (Şırnak)"),
    ("Tarsus Üniversitesi (Mersin)", "Tarsus Üniversitesi (Mersin)"),
    ("Ted Üniversitesi (Ankara)", "Ted Üniversitesi (Ankara)"),
    ("Tekirdağ Namık Kemal Üniversitesi (Tekirdağ)", "Tekirdağ Namık Kemal Üniversitesi (Tekirdağ)"),
    ("Tobb Ekonomi Ve Teknoloji Üniversitesi (Ankara)", "Tobb Ekonomi Ve Teknoloji Üniversitesi (Ankara)"),
    ("Tokat Gaziosmanpaşa Üniversitesi (Tokat)", "Tokat Gaziosmanpaşa Üniversitesi (Tokat)"),
    ("Toros Üniversitesi (Mersin)", "Toros Üniversitesi (Mersin)"),
    ("Trabzon Üniversitesi (Trabzon)", "Trabzon Üniversitesi (Trabzon)"),
    ("Trakya Üniversitesi (Edirne)", "Trakya Üniversitesi (Edirne)"),
    ("Türk Hava Kurumu Üniversitesi (Ankara)", "Türk Hava Kurumu Üniversitesi (Ankara)"),
    ("Türk-Alman Üniversitesi (İstanbul)", "Türk-Alman Üniversitesi (İstanbul)"),
    ("Ufuk Üniversitesi (Ankara)", "Ufuk Üniversitesi (Ankara)"),
    ("Uşak Üniversitesi (Uşak)", "Uşak Üniversitesi (Uşak)"),
    ("Üsküdar Üniversitesi (İstanbul)", "Üsküdar Üniversitesi (İstanbul)"),
    ("Van Yüzüncü Yıl Üniversitesi (Van)", "Van Yüzüncü Yıl Üniversitesi (Van)"),
    ("Yalova Üniversitesi (Yalova)", "Yalova Üniversitesi (Yalova)"),
    ("Yaşar Üniversitesi (İzmir)", "Yaşar Üniversitesi (İzmir)"),
    ("Yeditepe Üniversitesi (İstanbul)", "Yeditepe Üniversitesi (İstanbul)"),
    ("Yıldız Teknik Üniversitesi (İstanbul)", "Yıldız Teknik Üniversitesi (İstanbul)"),
    ("Yozgat Bozok Üniversitesi (Yozgat)", "Yozgat Bozok Üniversitesi (Yozgat)"),
    ("Yüksek İhtisas Üniversitesi (Ankara)", "Yüksek İhtisas Üniversitesi (Ankara)"),
    ("Zonguldak Bülent Ecevit Üniversitesi (Zonguldak)", "Zonguldak Bülent Ecevit Üniversitesi (Zonguldak)"),
]
