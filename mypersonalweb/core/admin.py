from django.contrib import admin
from . import models
# Register your models here.


class PDFDocumentAdmin(admin.ModelAdmin):
    ##shows fields in detail view
    ##
    fields=['name','description', 'document', 'uploaded_at',]
    readonly_fields=('uploaded_at',)
    search_fields= ['name']
    ##list_filter = ['uploaded_at']
    
    ##shows on list view
    ##
    list_display = ['name', 'description', 'uploaded_at']
    ## edit from list view
    list_editable = ['description']

admin.site.register(models.PDFDocument, PDFDocumentAdmin)
admin.site.register(models.ProjectsPost)
admin.site.register(models.User)

