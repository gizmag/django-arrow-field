import arrow
from django.db import models
from .model_fields import ArrowField


class TimeStampedModel(models.Model):
    created = ArrowField(default=arrow.utcnow)
    modified = ArrowField(auto_now=True)

    class Meta:
        abstract = True
