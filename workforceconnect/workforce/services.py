from django.db import IntegrityError, transaction
from django.core.exceptions import ValidationError

from .models import Application, JobOpportunity


class WorkerProfileRequired(Exception):
    pass


class JobClosed(Exception):
    pass


class DuplicateApplication(Exception):
    pass


def apply_for_job(user, job_id, cover_letter=""):
    with transaction.atomic():
        try:
            job = JobOpportunity.objects.select_for_update().get(id=job_id)
        except JobOpportunity.DoesNotExist:
            raise ValidationError("Job opportunity not found.")

        if not hasattr(user, "worker_profile"):
            raise WorkerProfileRequired(
                "You need a worker profile before applying for jobs."
            )

        worker = user.worker_profile

        if job.status != "open":
            raise JobClosed("This job opportunity is currently closed.")

        if Application.objects.filter(worker=worker, job=job).exists():
            raise DuplicateApplication(
                "You have already applied for this job."
            )

        try:
            application = Application.objects.create(
                worker=worker,
                job=job,
                cover_letter=cover_letter
            )
        except IntegrityError:
            raise DuplicateApplication(
                "You have already applied for this job."
            )

        return application


def close_job(job_id):
    with transaction.atomic():
        try:
            job = JobOpportunity.objects.select_for_update().get(id=job_id)
        except JobOpportunity.DoesNotExist:
            raise ValidationError("Job opportunity not found.")

        job.status = "closed"
        job.save(update_fields=["status"])

        return job


def reopen_job(job_id):
    with transaction.atomic():
        try:
            job = JobOpportunity.objects.select_for_update().get(id=job_id)
        except JobOpportunity.DoesNotExist:
            raise ValidationError("Job opportunity not found.")

        job.status = "open"
        job.save(update_fields=["status"])

        return job


def create_job_opportunity(
    employer,
    title,
    description,
    salary_range="",
    status="open"
):
    with transaction.atomic():
        if JobOpportunity.objects.filter(
            employer=employer,
            title__iexact=title
        ).exists():
            raise ValidationError(
                "This employer already has a job with the same title."
            )

        job = JobOpportunity.objects.create(
            employer=employer,
            title=title,
            description=description,
            salary_range=salary_range,
            status=status
        )

        return job