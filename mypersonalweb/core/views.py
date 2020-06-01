from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import PDFDocumentForm
from .models import PDFDocument
    
    
class SuccessTemplateView(generic.TemplateView):
    template_name = "core/success.html"
    



def PDF_form_upload(request):
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:success'))
    else:
        form = PDFDocumentForm()
    return render(request, 'core/upload_resume.html', {
        'form': form
    })
    
