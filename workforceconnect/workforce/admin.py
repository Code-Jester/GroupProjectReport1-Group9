from django.contrib import admin

from .models import (
    Skill,
    Worker,
    WorkerSkill,
    Employer,
    JobOpportunity,
    TrainingProgram,
    Application,
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "user",
        "experience_level",
        "availability",
    )
    list_filter = (
        "experience_level",
        "availability",
    )
    search_fields = (
        "full_name",
        "user__username",
        "user__email",
    )


@admin.register(WorkerSkill)
class WorkerSkillAdmin(admin.ModelAdmin):
    list_display = (
        "worker",
        "skill",
        "proficiency",
    )
    list_filter = (
        "proficiency",
    )
    search_fields = (
        "worker__full_name",
        "skill__name",
    )


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "user",
        "contact_email",
    )
    search_fields = (
        "company_name",
        "contact_email",
        "user__username",
    )


@admin.register(JobOpportunity)
class JobOpportunityAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "employer",
        "salary_range",
        "status",
        "created_at",
    )
    list_filter = (
        "status",
        "created_at",
    )
    search_fields = (
        "title",
        "description",
        "employer__company_name",
    )


@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "skill",
    )
    search_fields = (
        "title",
        "description",
        "skill__name",
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "worker",
        "job",
        "applied_at",
    )
    search_fields = (
        "worker__full_name",
        "job__title",
    )