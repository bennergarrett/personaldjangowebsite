from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from . import views


app_name='core'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('uploadresume/', views.PDF_form_upload, name='uploadresume'),
    path('success/', views.SuccessTemplateView.as_view(), name='success'),
    path('contact/', views.ContactTemplateView.as_view(), name='contact'),
    path('project_all/', views.ProjectListView.as_view(), name='project_all'),
    path('projectdetail/<int:pk>/', views.ProjectDetailView.as_view(), name='project_single'),
    path('create/', views.CreateProjectPostView.as_view(), name='create'),
    path('delete/<int:pk>', views.DeleteProjectPostView.as_view(), name='delete_post'),
    path('edit/<int:pk>', views.UpdateProjectPostView.as_view(), name='update_post'),
]


