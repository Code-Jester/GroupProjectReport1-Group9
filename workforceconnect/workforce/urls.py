from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workers/', views.WorkerListView.as_view(), name='worker_list'),
    path('workers/<int:pk>/', views.WorkerDetailView.as_view(), name='worker_detail'),
    path('employers/', views.EmployerListView.as_view(), name='employer_list'),
    path('jobs/', views.JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('training/', views.TrainingProgramListView.as_view(), name='training_list'),
    path('applications/', views.ApplicationListView.as_view(), name='application_list'),
]