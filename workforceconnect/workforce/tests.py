from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse

from .exceptions import DuplicateApplication, JobClosed, WorkerProfileRequired
from .models import (
    Application,
    Employer,
    JobOpportunity,
    Skill,
    TrainingProgram,
    Worker,
    WorkerSkill,
)
from .services import apply_for_job


class ModelRelationshipTest(TestCase):
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

    def test_model_string_methods_return_readable_names(self):
        training = TrainingProgram.objects.create(
            title="Python Basics",
            provider="CDU",
            target_skill=self.skill,
            duration_weeks=6
        )

        worker_skill = WorkerSkill.objects.create(
            worker=self.worker,
            skill=self.skill,
            proficiency_level="basic"
        )

        application = Application.objects.create(
            worker=self.worker,
            job_opportunity=self.job
        )

        self.assertEqual(str(self.skill), "Python")
        self.assertEqual(str(self.worker), "Worker One")
        self.assertEqual(str(self.employer), "Tech Darwin Pty Ltd")
        self.assertEqual(str(self.job), "Junior Django Developer")
        self.assertEqual(str(training), "Python Basics")
        self.assertEqual(str(worker_skill), "Worker One - Python")
        self.assertEqual(str(application), "Worker One -> Junior Django Developer")

    def test_worker_skill_relationship_connects_worker_and_skill(self):
        WorkerSkill.objects.create(
            worker=self.worker,
            skill=self.skill,
            proficiency_level="good"
        )

        self.assertIn(self.skill, self.worker.skills.all())

    def test_job_required_skills_relationship(self):
        self.job.required_skills.add(self.skill)

        self.assertIn(self.skill, self.job.required_skills.all())
        self.assertIn(self.job, self.skill.job_opportunities.all())

    def test_worker_cannot_apply_to_same_job_twice_at_database_level(self):
        Application.objects.create(
            worker=self.worker,
            job_opportunity=self.job
        )

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Application.objects.create(
                    worker=self.worker,
                    job_opportunity=self.job
                )


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

    def test_invalid_job_id_raises_validation_error(self):
        with self.assertRaises(ValidationError):
            apply_for_job(
                user=self.user,
                job_id=9999
            )


class ViewAndPermissionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="worker1",
            password="testpass123"
        )

        self.other_user = User.objects.create_user(
            username="worker2",
            password="testpass123"
        )

        self.no_profile_user = User.objects.create_user(
            username="visitor",
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

        self.other_worker = Worker.objects.create(
            user=self.other_user,
            name="Worker Two",
            email="worker2@example.com",
            phone="0411111111",
            experience_level="advanced",
            availability=True
        )

        self.employer = Employer.objects.create(
            organisation_name="Tech Darwin Pty Ltd",
            industry="Information Technology",
            location="Darwin, NT",
            contact_email="hr@techdarwin.com.au"
        )

        self.job = JobOpportunity.objects.create(
            employer=self.employer,
            title="Junior Django Developer",
            description="Develop and maintain Django web applications.",
            salary_range="70000 AUD",
            status="open"
        )

        self.other_job = JobOpportunity.objects.create(
            employer=self.employer,
            title="Data Assistant",
            description="Support workforce data entry.",
            salary_range="60000 AUD",
            status="open"
        )

    def test_home_page_loads_successfully(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "WorkforceConnect")
        self.assertContains(response, "System Overview")

    def test_application_list_requires_login(self):
        response = self.client.get(reverse("application_list"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_application_list_only_shows_logged_in_worker_applications(self):
        Application.objects.create(
            worker=self.worker,
            job_opportunity=self.job
        )

        Application.objects.create(
            worker=self.other_worker,
            job_opportunity=self.other_job
        )

        self.client.login(
            username="worker1",
            password="testpass123"
        )

        response = self.client.get(reverse("application_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Junior Django Developer")
        self.assertNotContains(response, "Data Assistant")

    def test_apply_job_requires_login(self):
        response = self.client.post(
            reverse("apply_job", args=[self.job.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)
        self.assertEqual(Application.objects.count(), 0)

    def test_logged_in_worker_can_apply_through_view(self):
        self.client.login(
            username="worker1",
            password="testpass123"
        )

        response = self.client.post(
            reverse("apply_job", args=[self.job.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Application.objects.count(), 1)
        self.assertTrue(
            Application.objects.filter(
                worker=self.worker,
                job_opportunity=self.job,
                status="pending"
            ).exists()
        )

    def test_user_without_worker_profile_cannot_apply_through_view(self):
        self.client.login(
            username="visitor",
            password="testpass123"
        )

        response = self.client.post(
            reverse("apply_job", args=[self.job.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Application.objects.count(), 0)


class APIAccessTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="apiuser",
            password="testpass123"
        )

        self.employer = Employer.objects.create(
            organisation_name="Tech Darwin Pty Ltd",
            industry="Information Technology",
            location="Darwin, NT",
            contact_email="hr@techdarwin.com.au"
        )

        self.open_job = JobOpportunity.objects.create(
            employer=self.employer,
            title="Open Job",
            description="This job should appear in the API.",
            salary_range="70000 AUD",
            status="open"
        )

        self.closed_job = JobOpportunity.objects.create(
            employer=self.employer,
            title="Closed Job",
            description="This job should not appear in the API.",
            salary_range="70000 AUD",
            status="closed"
        )

    def test_api_job_list_requires_authentication(self):
        response = self.client.get(reverse("api_job_list"))

        self.assertEqual(response.status_code, 403)

    def test_authenticated_api_only_returns_open_jobs(self):
        self.client.login(
            username="apiuser",
            password="testpass123"
        )

        response = self.client.get(reverse("api_job_list"))

        self.assertEqual(response.status_code, 200)

        response_text = response.content.decode()

        self.assertIn("Open Job", response_text)
        self.assertNotIn("Closed Job", response_text)