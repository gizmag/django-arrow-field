import arrow
from dateutil import tz
from django.test import TestCase
from arrow_field.model_fields import ArrowField

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
