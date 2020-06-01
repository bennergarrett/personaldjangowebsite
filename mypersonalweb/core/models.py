from django.db import models
from django.contrib import auth
from django.http import HttpResponseRedirect



# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    
    
    def __str__(self):
        
        ##username defiend with .User
        ##
        return "@{}".format(self.username)
    
    
class PDFDocument(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='resume/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description

    
