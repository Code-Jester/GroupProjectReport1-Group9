from django.conf import settings
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Worker(models.Model):
    EXPERIENCE_LEVELS = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="worker_profile"
    )
    full_name = models.CharField(max_length=150)
    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_LEVELS,
        default="beginner"
    )
    availability = models.BooleanField(default=True)
    skills = models.ManyToManyField(
        Skill,
        through="WorkerSkill",
        blank=True
    )

    def __str__(self):
        return self.full_name


class WorkerSkill(models.Model):
    PROFICIENCY_LEVELS = [
        ("basic", "Basic"),
        ("good", "Good"),
        ("expert", "Expert"),
    ]

    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency = models.CharField(
        max_length=20,
        choices=PROFICIENCY_LEVELS,
        default="basic"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["worker", "skill"],
                name="unique_worker_skill"
            )
        ]

    def __str__(self):
        return f"{self.worker} - {self.skill} ({self.proficiency})"


class Employer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employer_profile",
        null=True,
        blank=True
    )
    company_name = models.CharField(max_length=150, unique=True)
    contact_email = models.EmailField()

    def __str__(self):
        return self.company_name


class JobOpportunity(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("closed", "Closed"),
    ]

    title = models.CharField(max_length=150)
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        related_name="jobs"
    )
    description = models.TextField()
    salary_range = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="open"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["employer", "title"],
                name="unique_employer_job_title"
            )
        ]

    def __str__(self):
        return f"{self.title} - {self.employer}"


class TrainingProgram(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="training_programs"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "skill"],
                name="unique_training_program_skill"
            )
        ]

    def __str__(self):
        return self.title


class Application(models.Model):
    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    job = models.ForeignKey(
        JobOpportunity,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["worker", "job"],
                name="unique_worker_job_application"
            )
        ]

    def __str__(self):
        return f"{self.worker} applied for {self.job}"