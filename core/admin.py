from django.contrib import admin
from .models import Youth, Program, Participation


@admin.register(Youth)
class YouthAdmin(admin.ModelAdmin):
    list_display = ('case_id', 'first_name', 'last_name', 'age', 'risk_level')
    search_fields = ('case_id', 'first_name', 'last_name', 'risk_level')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'program_type')
    search_fields = ('name', 'program_type')


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('youth', 'program', 'start_date', 'status')
    list_filter = ('status', 'program')