from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('youths/', views.youth_list),
    path('youths/add/', views.add_youth),
    path('programs/', views.program_list),
    path('participations/', views.participation_list),
]