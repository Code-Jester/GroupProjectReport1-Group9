from django.contrib import admin
from .models import Skill, Worker, WorkerSkill, Employer, JobOpportunity, TrainingProgram, Application

admin.site.register(Skill)
admin.site.register(Worker)
admin.site.register(WorkerSkill)
admin.site.register(Employer)
admin.site.register(JobOpportunity)
admin.site.register(TrainingProgram)
admin.site.register(Application)