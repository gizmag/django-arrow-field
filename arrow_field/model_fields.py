import arrow
from django.db.models import DateTimeField, SubfieldBase
from .form_fields import ArrowField as ArrowFormField


class ArrowField(DateTimeField):
    __metaclass__ = SubfieldBase

    def get_internal_type(self):
        return "ArrowField"

    def to_python(self, value):
        if isinstance(value, arrow.Arrow):
            return value

        value = super(ArrowField, self).to_python(value)

        if value:
            return arrow.get(value)

    def get_prep_value(self, value):
        if value:
            return value.datetime

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return '' if value is None else value.isoformat()

    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            value = arrow.utcnow()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(ArrowField, self).pre_save(model_instance, add)

    def formfield(self, **kwargs):
        defaults = {'form_class': ArrowFormField}
        defaults.update(kwargs)
        return super(ArrowField, self).formfield(**defaults)
