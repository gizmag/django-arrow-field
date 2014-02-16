from __future__ import unicode_literals
from django.db import models
from arrow_field.model_fields import ArrowField


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    birthday = ArrowField()


class PersonAutoNow(models.Model):
    first_name = models.CharField(max_length=100)
    birthday = ArrowField(auto_now=True)


class PersonAutoNowAdd(models.Model):
    first_name = models.CharField(max_length=100)
    birthday = ArrowField(auto_now_add=True)
