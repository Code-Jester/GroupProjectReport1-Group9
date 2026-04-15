from django.shortcuts import render, redirect
from .models import Youth, Program, Participation

# Home dashboard
def home(request):
    context = {
        'youth_count': Youth.objects.count(),
        'program_count': Program.objects.count(),
        'participation_count': Participation.objects.count(),
    }
    return render(request, 'core/home.html', context)

# Youth list
def youth_list(request):
    youths = Youth.objects.all()
    return render(request, 'core/youth_list.html', {'youths': youths})

# Add youth
def add_youth(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        case_id = request.POST.get('case_id')
        risk_level = request.POST.get('risk_level')

        Youth.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            case_id=case_id,
            risk_level=risk_level
        )
        return redirect('/youths/')

    return render(request, 'core/add_youth.html')

# Program list
def program_list(request):
    programs = Program.objects.all()
    return render(request, 'core/program_list.html', {'programs': programs})

# Participation list
def participation_list(request):
    participations = Participation.objects.all()
    return render(request, 'core/participation_list.html', {'participations': participations})