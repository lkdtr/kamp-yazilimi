from django.apps import AppConfig


class UserProfileAppConfig(AppConfig):
    name = 'userprofile'

    def ready(self):
        import userprofile.signals