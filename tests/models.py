from django.db import models
from arrow_field.model_fields import ArrowField


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    birthday = ArrowField()
