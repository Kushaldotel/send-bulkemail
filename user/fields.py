# fields.py
from django.forms import FileField
from django.core.exceptions import ValidationError
from .widgets import MultiFileInput

class MultiFileField(FileField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = kwargs.get('widget', MultiFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        # If no files are uploaded, return the initial value
        if not data and initial:
            return initial

        # Ensure that the uploaded files are valid
        if not data or not isinstance(data, list):
            raise ValidationError("You must upload one or more files.")

        return data
