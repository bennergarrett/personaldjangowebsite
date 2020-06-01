from django.contrib.auth import get_user_model
from .models import PDFDocument
from django import forms
##if i want user to be able to create an account
##
##from django.contrib.auth.forms import UserCreationForm

from django import forms

class PDFDocumentForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ('description', 'document', )
        

# class PDFDocumentForm(forms.Form):
#     docfile = forms.FileField(
#         label='Select a file',
#         help_text='max. 42 megabytes'
#     )