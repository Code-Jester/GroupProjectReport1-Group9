from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Worker(models.Model):
    EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    availability = models.BooleanField(default=True)
    skills = models.ManyToManyField(Skill, through='WorkerSkill')

    def __str__(self):
        return self.name


class WorkerSkill(models.Model):
    PROFICIENCY_CHOICES = [
        ('basic', 'Basic'),
        ('good', 'Good'),
        ('expert', 'Expert'),
    ]

    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency_level = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES)

    def __str__(self):
        return f"{self.worker.name} - {self.skill.name}"


class Employer(models.Model):
    organisation_name = models.CharField(max_length=150)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __str__(self):
        return self.organisation_name


class JobOpportunity(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=150)
    description = models.TextField()
    required_skills = models.ManyToManyField(Skill, related_name='job_opportunities')
    salary_range = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return self.title


class TrainingProgram(models.Model):
    title = models.CharField(max_length=150)
    provider = models.CharField(max_length=150)
    target_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='training_programs')
    duration_weeks = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='applications')
    job_opportunity = models.ForeignKey(JobOpportunity, on_delete=models.CASCADE, related_name='applications')
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.worker.name} -> {self.job_opportunity.title}"