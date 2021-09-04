from django import forms
from .models import Document
#DataFlair #File_Upload
class Document_Form(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
        'name',
        'description',
        'filetype',
        'document',
        ]