from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView

from .exceptions import DuplicateApplication, JobClosed, WorkerProfileRequired
from .models import Worker, Employer, JobOpportunity, TrainingProgram, Application
from .services import apply_for_job


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


class ApplyForJobView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            apply_for_job(user=request.user, job_id=pk)
            messages.success(request, "Application submitted successfully.")

        except WorkerProfileRequired as e:
            messages.error(request, str(e))

        except JobClosed as e:
            messages.warning(request, str(e))

        except DuplicateApplication as e:
            messages.warning(request, str(e))

        except ValidationError as e:
            messages.error(request, str(e))

        return redirect('job_detail', pk=pk)


class TrainingProgramListView(ListView):
    model = TrainingProgram
    template_name = 'workforce/training_list.html'
    context_object_name = 'training_programs'


class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'workforce/application_list.html'
    context_object_name = 'applications'

    def get_queryset(self):
        if hasattr(self.request.user, 'worker_profile'):
            return Application.objects.filter(
                worker=self.request.user.worker_profile
            )

        return Application.objects.none()
