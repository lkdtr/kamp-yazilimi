#!/usr/bin/python

from django.contrib import admin
from mailing.models import EmailTemplate


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['operation_name', 'subject', 'site']
