from django.core.exceptions import ValidationError
from django.db import transaction

from .exceptions import DuplicateApplication, JobClosed, WorkerProfileRequired
from .models import Application, JobOpportunity


def apply_for_job(user, job_id):
    """
    Orchestrates the full job application workflow across Worker,
    JobOpportunity and Application.

    This service coordinates multiple models in one business operation:
    it checks that the authenticated user has a Worker profile, verifies
    that the selected job is open, prevents duplicate applications, and
    creates a new Application record atomically.

    Args:
        user (User): The authenticated Django user applying for the job.
        job_id (int): The primary key of the JobOpportunity.

    Returns:
        Application: The newly created Application instance.

    Raises:
        WorkerProfileRequired: If the user does not have a Worker profile.
        JobClosed: If the selected job opportunity is not open.
        DuplicateApplication: If the worker has already applied for the job.
        ValidationError: If the job opportunity does not exist.
    """
    with transaction.atomic():
        if not hasattr(user, 'worker_profile'):
            raise WorkerProfileRequired(
                "You need a worker profile before applying for jobs."
            )

        worker = user.worker_profile

        try:
            job = JobOpportunity.objects.select_for_update().get(pk=job_id)
        except JobOpportunity.DoesNotExist:
            raise ValidationError("Job opportunity not found.")

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