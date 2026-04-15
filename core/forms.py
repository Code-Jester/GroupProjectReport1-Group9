from django import forms
from .models import Youth, Program, Participation


class YouthForm(forms.ModelForm):
    class Meta:
        model = Youth
        fields = ['first_name', 'last_name', 'age', 'case_id', 'risk_level']


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'program_type', 'description']


class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ['youth', 'program', 'start_date', 'status']