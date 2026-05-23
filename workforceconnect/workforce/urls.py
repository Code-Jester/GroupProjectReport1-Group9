from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .api import JobOpportunityListAPIView


urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Authentication
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='workforce/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # Workers
    path(
        'workers/',
        views.WorkerListView.as_view(),
        name='worker_list'
    ),

    path(
        'workers/<int:pk>/',
        views.WorkerDetailView.as_view(),
        name='worker_detail'
    ),

    # Employers
    path(
        'employers/',
        views.EmployerListView.as_view(),
        name='employer_list'
    ),

    # Jobs
    path(
        'jobs/',
        views.JobListView.as_view(),
        name='job_list'
    ),

    path(
        'jobs/<int:pk>/',
        views.JobDetailView.as_view(),
        name='job_detail'
    ),

    path(
        'jobs/<int:pk>/apply/',
        views.ApplyForJobView.as_view(),
        name='apply_job'
    ),

    # Training
    path(
        'training/',
        views.TrainingProgramListView.as_view(),
        name='training_list'
    ),

    # Applications
    path(
        'applications/',
        views.ApplicationListView.as_view(),
        name='application_list'
    ),

    # REST API
    path(
        'api/jobs/',
        JobOpportunityListAPIView.as_view(),
        name='api_job_list'
    ),
]