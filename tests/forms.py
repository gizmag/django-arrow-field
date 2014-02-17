from django.forms import ModelForm

from .models import Person
from arrow_field.form_fields import ISO8601ArrowField


class PersonForm(ModelForm):
    class Meta:
        model = Person


class ISO8601PersonForm(ModelForm):
    birthday = ISO8601ArrowField()
    class Meta:
        model = Person
