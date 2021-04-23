from django import forms
from .models import FileMessage


class FileForm(forms.ModelForm):
    class Meta:
        model = FileMessage
        fields = ('file',)
