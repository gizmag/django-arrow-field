from __future__ import unicode_literals
import arrow
from dateutil import tz
from django.test import TestCase
from django.core import serializers

from arrow_field.model_fields import ArrowField
from arrow_field.form_fields import ArrowField as ArrowFormField


from .forms import PersonForm, ISO8601PersonForm
from .models import Person, PersonAutoNow, PersonAutoNowAdd


class ArrowModelFieldTests(TestCase):
    def setUp(self):
        self.person = Person.objects.create(
            first_name='John',
            birthday=arrow.get(2000, 6, 1),
        )

    def test_retrieved_model_returns_arrow_instance(self):
        person = Person.objects.get()
        self.assertEqual(person.birthday, arrow.get(2000, 6, 1))

    def test_arrow_instance_can_be_set_to_model_field(self):
        person = Person.objects.get()
        person.birthday = arrow.get(1990, 6, 1)
        person.save()
        self.assertEqual(person.birthday, arrow.get(1990, 6, 1))

    def test_auto_now_works_correctly(self):
        person = PersonAutoNow(first_name='James')
        person.save()
        self.assertTrue(isinstance(person.birthday, arrow.Arrow))

        first_birthday = person.birthday

        person.save()

        self.assertGreater(person.birthday, first_birthday)

    def test_auto_now_add_works_correctly(self):
        person = PersonAutoNowAdd(first_name='Jason')
        person.save()
        self.assertTrue(isinstance(person.birthday, arrow.Arrow))

        first_birthday = person.birthday

        person.save()

        self.assertEqual(person.birthday, first_birthday)

    def test_field_lookups_work_correctly(self):
        self.assertEqual(
            Person.objects.filter(birthday__gt=arrow.get(1990, 6, 1)).count(),
            1
        )

        self.assertEqual(
            Person.objects.filter(birthday__lt=arrow.get(1990, 6, 1)).count(),
            0
        )

        self.assertEqual(
            Person.objects.filter(birthday__lt=arrow.get(2010, 6, 1)).count(),
            1
        )

        self.assertEqual(
            Person.objects.filter(birthday__year=2000).count(),
            1
        )

        self.assertEqual(
            Person.objects.filter(birthday__year=2001).count(),
            0
        )

    def test_arrowfield_serializes_correctly(self):
        data = serializers.serialize("json", Person.objects.all())
        result = list(serializers.deserialize("json", data))
        self.assertEqual(result[0].object.birthday, arrow.get(2000, 6, 1))


class ArrowFormFieldTests(TestCase):
    def setUp(self):
        self.person = Person.objects.create(
            first_name='John',
            birthday=arrow.get(2000, 6, 1),
        )
        self.form = PersonForm(instance=self.person)

    def test_arrow_form_field_automatically_used_on_modelform(self):
        self.assertEqual(self.form.fields['birthday'].__class__, ArrowFormField)

    def test_form_renders_correctly(self):
        # should not except
        self.form.as_p()

    def test_form_strptime_works(self):
        date_string = arrow.get(2010, 6, 1).format('YYYY-MM-DD HH:mm:ss')
        form = PersonForm({'first_name': 'Greg', 'birthday': date_string}, instance=self.person)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['birthday'], arrow.get(2010, 6, 1))

    def test_iso8601_form_field_works(self):
        date_string = arrow.get(2010, 6, 1).isoformat()
        form = ISO8601PersonForm({'first_name': 'Greg', 'birthday': date_string}, instance=self.person)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['birthday'], arrow.get(2010, 6, 1))
