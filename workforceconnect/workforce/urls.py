from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),

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

    path('workers/', views.WorkerListView.as_view(), name='worker_list'),

    path(
        'workers/<int:pk>/',
        views.WorkerDetailView.as_view(),
        name='worker_detail'
    ),

    path(
        'employers/',
        views.EmployerListView.as_view(),
        name='employer_list'
    ),

    path('jobs/', views.JobListView.as_view(), name='job_list'),

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

    path(
        'training/',
        views.TrainingProgramListView.as_view(),
        name='training_list'
    ),

    path(
        'applications/',
        views.ApplicationListView.as_view(),
        name='application_list'
    ),
]