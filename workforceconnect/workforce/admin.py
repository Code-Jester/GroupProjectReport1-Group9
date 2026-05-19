from django.contrib import admin

from .models import (
    Skill,
    Worker,
    WorkerSkill,
    Employer,
    JobOpportunity,
    TrainingProgram,
    Application
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category')


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'experience_level',
        'availability'
    )

    list_filter = (
        'experience_level',
        'availability'
    )

    search_fields = (
        'name',
        'email'
    )


@admin.register(WorkerSkill)
class WorkerSkillAdmin(admin.ModelAdmin):
    list_display = (
        'worker',
        'skill',
        'proficiency_level'
    )

    list_filter = (
        'proficiency_level',
    )


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        'organisation_name',
        'industry',
        'location'
    )

    search_fields = (
        'organisation_name',
        'industry'
    )


@admin.register(JobOpportunity)
class JobOpportunityAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'employer',
        'salary_range',
        'status'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'title',
        'description'
    )


@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'provider',
        'duration_weeks'
    )

    search_fields = (
        'title',
        'provider'
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'worker',
        'job_opportunity',
        'status',
        'application_date'
    )

    list_filter = (
        'status',
    )