from django.shortcuts import render, redirect,get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import PDFDocument
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
User = get_user_model()

from django.utils import timezone
from .forms import PDFDocumentForm, PostForm
from .models import ProjectsPost


##test url to show upload was success
##  
class SuccessTemplateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "core/success.html"
    
    def get_object(self):
        return self.request.user

class ContactTemplateView(generic.TemplateView):
    template_name = "core/contact.html"
    
    # def get_object(self):
    #     return self.request.user

class ProjectListView(generic.ListView):
    paginate_by = 5  # if pagination is desired
    model = ProjectsPost
    # template_name = "core/project_list.html"
    select_related = ('user', 'title', 'message', 'created_at')
   
    # select_related = ['user', 'message']
    
    # def get_queryset(self):
        # context = super(BookListView, self).get_context_data(**kwargs)
        # return ProjectsPost.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')
    
    
#@login_required
class CreateProjectPostView(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    
    ##redirect to login or detail view
    ##
    login_url= reverse_lazy('core:login')
    edirect_field_name = reverse_lazy('core:project_single')
    
    ##use form created to create post
    ##
    form_class= PostForm
    
    ##use model
    ##
    model = ProjectsPost
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user= self.request.user
        self.object.save()
        return super().form_valid(form)
    
class UpdateProjectPostView(LoginRequiredMixin, generic.UpdateView):
    login_url='/login/'
    redirect_field_name = reverse_lazy('project_single')
    form_class = PostForm
    model = ProjectsPost
    
class DeleteProjectPostView(LoginRequiredMixin, generic.DeleteView):
     model = ProjectsPost
     ##where to go after deleting
     ##
     success_url = reverse_lazy('core:project_all')
    
    

class ProjectDetailView(generic.DetailView):
    # template_name= 'core/projectpost_detail.html'
    model= ProjectsPost
    
    # def get_object(self, queryset=None):
    #     return get_object_or_404(PDFDocument, pk=pk)


##uploads PDF to resumes section
##

@login_required
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
   
