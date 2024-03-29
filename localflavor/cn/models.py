from django.db.models import CharField
from django.utils.translation import gettext_lazy as _
from .forms import CNIDCardField as CNIDCardFieldFormField


class CNIDCardField(CharField):
    """
    A model field that stores a Resident Identity Card (PRC) number

    Form represent it as ``forms.CNIDCardField`` field.
    """
    description = _("ID Card Number")

    def __init__(self, max_length=18, *args, **kwargs):
        kwargs['max_length'] = max_length
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': CNIDCardFieldFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
