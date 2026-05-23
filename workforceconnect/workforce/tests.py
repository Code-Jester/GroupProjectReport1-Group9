from django.test import TestCase

from django.test import TestCase
from django.contrib.auth.models import User

from .exceptions import DuplicateApplication, JobClosed, WorkerProfileRequired
from .models import Application, Employer, JobOpportunity, Skill, Worker
from .services import apply_for_job


class ApplyForJobServiceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="worker1",
            password="testpass123"
        )

        self.worker = Worker.objects.create(
            user=self.user,
            name="Worker One",
            email="worker1@example.com",
            phone="0400000000",
            experience_level="beginner",
            availability=True
        )

        self.employer = Employer.objects.create(
            organisation_name="Tech Darwin Pty Ltd",
            industry="Information Technology",
            location="Darwin, NT",
            contact_email="hr@techdarwin.com.au"
        )

        self.skill = Skill.objects.create(
            name="Python",
            category="Programming"
        )

        self.job = JobOpportunity.objects.create(
            employer=self.employer,
            title="Junior Django Developer",
            description="Develop and maintain Django web applications.",
            salary_range="70000 AUD",
            status="open"
        )

        self.job.required_skills.add(self.skill)

    def test_successful_application_creates_pending_application(self):
        application = apply_for_job(
            user=self.user,
            job_id=self.job.pk
        )

        self.assertEqual(Application.objects.count(), 1)
        self.assertEqual(application.worker, self.worker)
        self.assertEqual(application.job_opportunity, self.job)
        self.assertEqual(application.status, "pending")

    def test_duplicate_application_raises_duplicate_application(self):
        apply_for_job(
            user=self.user,
            job_id=self.job.pk
        )

        with self.assertRaises(DuplicateApplication):
            apply_for_job(
                user=self.user,
                job_id=self.job.pk
            )

    def test_closed_job_raises_job_closed(self):
        self.job.status = "closed"
        self.job.save()

        with self.assertRaises(JobClosed):
            apply_for_job(
                user=self.user,
                job_id=self.job.pk
            )

    def test_user_without_worker_profile_raises_worker_profile_required(self):
        user_without_profile = User.objects.create_user(
            username="no_profile",
            password="testpass123"
        )

        with self.assertRaises(WorkerProfileRequired):
            apply_for_job(
                user=user_without_profile,
                job_id=self.job.pk
            )