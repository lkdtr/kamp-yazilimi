#!/usr/bin/env python
import hashlib

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from userprofile.models import UserProfile

from mudur.models import Site, Question, Answer, TextBoxQuestions
from mudur.settings import TRAINESS_PARTICIPATION_STATE


def make_choices(choices):
    return tuple([(k, _(v)) for k, v in choices.items()])


class Course(models.Model):
    no = models.CharField(verbose_name=_("Course No"), max_length=4)
    name = models.CharField(verbose_name=_("Course Name"), max_length=255)
    description = models.TextField(verbose_name=_("Description"))
    trainess = models.ManyToManyField(UserProfile, related_name="trainess", verbose_name=_("Trainess"), blank=True)
    trainer = models.ManyToManyField(UserProfile, related_name="trainer", verbose_name=_("Trainer"))
    authorized_trainer = models.ManyToManyField(UserProfile, related_name="authorized_trainer",
                                                verbose_name=_("Authorized Trainers"))
    approved = models.BooleanField(default=False)
    application_is_open = models.BooleanField(default=True)
    site = models.ForeignKey(Site)
    url = models.CharField(verbose_name=_("URL"), max_length=350)
    question = models.ManyToManyField(Question, blank=True, verbose_name=_("Question"))
    textboxquestion = models.ManyToManyField(TextBoxQuestions, blank=True, verbose_name=_("Text Box Questions"))
    max_participant = models.IntegerField(default=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


class TrainessCourseRecord(models.Model):
    trainess = models.ForeignKey(UserProfile)
    course = models.ForeignKey(Course)
    preference_order = models.SmallIntegerField(default=1)
    approved = models.BooleanField(default=False)
    trainess_approved = models.BooleanField(default=False)
    instapprovedate = models.DateField(default=now, blank=True, null=True)
    consentemailsent = models.BooleanField(default=False)

    def __str__(self):
        return self.course.name

    class Meta:
        verbose_name = _('Trainess Course Record')
        verbose_name_plural = _('Trainess Course Records')
        ordering = ['trainess', 'preference_order']


class TrainessParticipation(models.Model):
    courserecord = models.ForeignKey(TrainessCourseRecord)
    morning = models.CharField(choices=TRAINESS_PARTICIPATION_STATE, verbose_name=_("Morning"), max_length=3,
                               default='0')
    afternoon = models.CharField(choices=TRAINESS_PARTICIPATION_STATE, verbose_name=_("Afternoon"), max_length=3,
                                 default='0')
    evening = models.CharField(choices=TRAINESS_PARTICIPATION_STATE, verbose_name=_("Evening"), max_length=3,
                               default='0')
    day = models.CharField(verbose_name=_("Day"), max_length=20, default='1')

    def __str__(self):
        return self.courserecord.trainess.user.username

    class Meta:
        verbose_name = _('Trainess Participation Information')
        verbose_name_plural = _('Trainess Participation Information')


class TrainessTestAnswers(models.Model):
    tcourserecord = models.ForeignKey(TrainessCourseRecord)
    answer = models.ManyToManyField(Answer)

    def __str__(self):
        return self.tcourserecord.trainess.user.username

    class Meta:
        verbose_name = _('Trainess Test Answer')
        verbose_name_plural = _('Trainess Test Answer')


class Certificate(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    course_name = models.TextField(max_length=200)
    camp_year = models.IntegerField(default=0)
    camp_semester = models.CharField(max_length=5)
    signature = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if self.id is None:
            user = self.user_profile.user
            # Generate Signature
            sign = user.first_name + user.last_name + str(user.id) + str(self.camp_year) + str(self.camp_semester)
            sign = sign.encode()
            self.signature = hashlib.sha256(sign).hexdigest()
        super(Certificate, self).save(*args, **kwargs)