import arrow
from django.forms import DateTimeField


class ArrowField(DateTimeField):
    def to_python(self, value):
        if isinstance(value, arrow.Arrow):
            return value
        return super(ArrowField, self).to_python(value)

    def strptime(self, value, format):
        return arrow.get(value, format)
