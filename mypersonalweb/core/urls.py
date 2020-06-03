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
    path('post/all', views.ProjectListView.as_view(), name='project_all'),
    path('post/<int:pk>/', views.ProjectDetailView.as_view(), name='project_single'),
    path('post/create/', views.CreateProjectPostView.as_view(), name='create'),
    path('post/<int:pk>/delete/', views.DeleteProjectPostView.as_view(), name='delete_post'),
    path('post/<int:pk>/edit/', views.UpdateProjectPostView.as_view(), name='update_post'),
]


