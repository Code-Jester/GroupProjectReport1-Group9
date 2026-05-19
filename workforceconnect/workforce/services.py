from django.db import transaction

from .exceptions import DuplicateApplication, JobClosed, WorkerProfileRequired
from .models import Application, JobOpportunity


def apply_for_job(user, job_id):
    with transaction.atomic():
        if not hasattr(user, 'worker_profile'):
            raise WorkerProfileRequired(
                "You need a worker profile before applying for jobs."
            )

        worker = user.worker_profile
        job = JobOpportunity.objects.select_for_update().get(pk=job_id)

        if job.status != 'open':
            raise JobClosed(
                "This job opportunity is currently closed."
            )

        already_applied = Application.objects.filter(
            worker=worker,
            job_opportunity=job
        ).exists()

        if already_applied:
            raise DuplicateApplication(
                "You have already applied for this job."
            )

        return Application.objects.create(
            worker=worker,
            job_opportunity=job,
            status='pending'
        )