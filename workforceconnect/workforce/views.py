from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Worker, Employer, JobOpportunity, TrainingProgram, Application


def home(request):
    context = {
        'worker_count': Worker.objects.count(),
        'employer_count': Employer.objects.count(),
        'job_count': JobOpportunity.objects.count(),
        'training_count': TrainingProgram.objects.count(),
        'application_count': Application.objects.count(),
    }
    return render(request, 'workforce/home.html', context)


class WorkerListView(ListView):
    model = Worker
    template_name = 'workforce/worker_list.html'
    context_object_name = 'workers'


class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'workforce/worker_detail.html'
    context_object_name = 'worker'


class EmployerListView(ListView):
    model = Employer
    template_name = 'workforce/employer_list.html'
    context_object_name = 'employers'


class JobListView(ListView):
    model = JobOpportunity
    template_name = 'workforce/job_list.html'
    context_object_name = 'jobs'


class JobDetailView(DetailView):
    model = JobOpportunity
    template_name = 'workforce/job_detail.html'
    context_object_name = 'job'


class TrainingProgramListView(ListView):
    model = TrainingProgram
    template_name = 'workforce/training_list.html'
    context_object_name = 'training_programs'


class ApplicationListView(ListView):
    model = Application
    template_name = 'workforce/application_list.html'
    context_object_name = 'applications'