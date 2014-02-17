from __future__ import unicode_literals
import arrow
from django.forms import DateTimeField


class ArrowField(DateTimeField):
    input_formats = [
        'YYYY-MM-DD HH:mm:ss',
        'YYYY-MM-DD HH:mm',
        'YYYY-MM-DD',
        'MM/DD/YYYY HH:mm:ss',
        'MM/DD/YYYY HH:mm',
        'MM/DD/YYYY',
        'MM/DD/YY HH:mm:ss',
        'MM/DD/YY HH:mm',
        'MM/DD/YY',
    ]

    def to_python(self, value):
        if isinstance(value, arrow.Arrow):
            return value
        return super(ArrowField, self).to_python(value)

    def strptime(self, value, format):
        return arrow.get(value, format)


class ISO8601ArrowField(ArrowField):
    input_formats = ['iso-8601']

    def strptime(self, value, format):
        if format == 'iso-8601':
            return arrow.get(value)
