import hashlib
import logging
import random

from django.contrib.auth.tokens import default_token_generator
from mailing.models import EmailTemplate

from mudur.adaptor import send_email
from mudur.settings import EMAIL_FROM_ADDRESS

log = logging.getLogger(__name__)


def create_verification_link(user):
    return default_token_generator.make_token(user)


def send_email_by_operation_name(context, operation_name):
    try:
        emailtemplate = EmailTemplate.objects.get(operation_name=operation_name)
        send_email(
            emailtemplate.subject, emailtemplate.body_html, context, EMAIL_FROM_ADDRESS, context["recipientlist"]
        )
        return 1
    except Exception as e:
        log.error(str(e), extra={"clientip": context.get("clientip", ""), "user": context.get("user", "")})
        return 0
