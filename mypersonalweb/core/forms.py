from django.contrib.auth import get_user_model
from .models import PDFDocument
from django import forms

from .models import ProjectsPost
##if i want user to be able to create an account
##
##from django.contrib.auth.forms import UserCreationForm


class PDFDocumentForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ('name', 'description', 'document', )
        
        
class PostForm(forms.ModelForm):
    class Meta:
        ##model form is based off on
        ##
        model = ProjectsPost
        
        ##fields user can interact with
        ##
        fields = ('author', 'title', 'message')
        
        ##used to overwrite default values
        ##
        widgets ={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'message':forms.Textarea(attrs={'class':'medium-editor-textarea'}),
        }
        