#!/usr/bin/env python

from django.db import models
from mudur.models import Site


class EmailTemplate(models.Model):
    operation_name = models.CharField(unique=True, null=False, max_length=200, verbose_name="Fonksiyon ismi")
    subject = models.CharField(max_length=300, verbose_name="Konu")
    body_html = models.TextField(max_length=2000, verbose_name="HTML E-posta Govdesi")
    site = models.ForeignKey(Site)

    def __str__(self):
        return self.operation_name

    class Meta:
        verbose_name = 'E-posta sablonu'
        verbose_name_plural = 'E-posta sablonlari'
