# Django Arrow Field

[![Build Status](https://travis-ci.org/gizmag/django-arrow-field.png?branch=master)](https://travis-ci.org/gizmag/django-arrow-field)
[![Code Health](https://landscape.io/github/gizmag/django-arrow-field/master/landscape.png)](https://landscape.io/github/gizmag/django-arrow-field/master)

Django Arrow Field is a custom model field that represents dates stored in the
database as `Arrow` instances instead of `datetime`'s.
[Arrow](http://crsmithdev.com/arrow/) is a wonderful datetime library with a
much saner API than the standard library `datetime`.
`ArrowField` is a drop-in replacement.

## Installation

```bash
pip install django-arrow-field
```

## Usage

### Models

To use it in your models it's a simply case of declaring the field on your model
class.

```python
from django.db import models
from arrow_field.model_fields import ArrowField


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    birthday = ArrowField()
```

Then you just use it the same way you would any other model field.

```python
import arrow

person = Person.objects.create(
    first_name='Jacob',
    birthday=arrow.get(1994, 11, 7)
)

person.birthday
# <Arrow [1994-11-07T00:00:00+00:00]>

person = Person.objects.get(birthday=arrow.get(1994, 11, 7))
person.first_name
# Jacob
```

## Forms

By default `ModelForm`'s will use the `ArrowField` form field for arrow fields.
`ArrowField` subclasses `DateTimeField` and is functionally equivalent. You can
override it with any option that is valid for `DateTimeField`.

```python
from django.forms import ModelForm

from .models import Person
from arrow_field.form_fields import ArrowField


class PersonForm(ModelForm):
    birthday = ArrowField(help_text='Enter your birthday')

    class Meta:
        model = Person
```

You can also use `ISO8601ArrowField` to accept ISO8601 timestamps, for example
`1994-11-07T00:00:00+00:00`. This is useful when receiving timestamps from
javascript.

```python
from django.forms import ModelForm

from .models import Person
from arrow_field.form_fields import ISO8601ArrowField


class PersonForm(ModelForm):
    birthday = ISO8601ArrowField()

    class Meta:
        model = Person
```


## Caveats

- The queryset `datetimes()` method returns a `datetime` instance, not an
`Arrow`
