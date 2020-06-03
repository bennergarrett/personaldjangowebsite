from django.db import models
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.db.models.signals import pre_save
from .storage import OverwriteStorage
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth import get_user_model
User1 = get_user_model()
##allows for markdown / links in post
##
import misaka
import os

from django.conf import settings
from django.core.files.storage import Storage

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
       
    def __str__(self):
        ##username defiend with .User
        ##
        return "@{}".format(self.username)


class PDFDocument(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Document')
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='resume/', storage=OverwriteStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

##post project should only work for auth.User
##will need to make sure it only works with admin
##
class ProjectsPost(models.Model):
    author = models.ForeignKey(User1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, default='Post Title')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    ##need to add image file
    ##
    
    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)
        
    ##this goes to detail View
    ##
    def get_absolute_url(self):
        return reverse("core:project_single", kwargs={
                                               'pk':self.pk})
        
    class Meta:
        ##shows most recent first
        ##
        ordering= ['-created_at']
        
        ##every message is uniquely linked to user
        ##
        unique_together = ['author', 'message']
