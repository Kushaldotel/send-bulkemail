# forms.py
from django import forms
from .fields import MultiFileField

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter email subject'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'rich-text-editor'}))
    attachments = MultiFileField(required=False)  # Use the custom multi-file field
