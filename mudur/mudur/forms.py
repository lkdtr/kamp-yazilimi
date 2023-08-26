from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError, MultipleObjectsReturned
from django.forms import EmailField

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": _("Lütfen doğru e-posta ve parola girin. Her iki alanında büyük küçük harfe duyarlı"
                           " olabileceğini unutmayın."),
        "inactive": _("Bu hesap aktif değil."),
    }

    username = EmailField(
        label='E-posta',
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = self.authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        except MultipleObjectsReturned:
            user = User.objects.filter(email=username).order_by('id').first()
        if user.check_password(password):
            return user
        return None

    def get_invalid_login_error(self):
        return ValidationError(self.error_messages["invalid_login"], code="invalid_login")
