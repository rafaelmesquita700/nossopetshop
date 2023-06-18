from django.urls import path
from . import views

urlpatterns = [
    path('', views.agendamentos, name='agendamentos'),
    path('processa_agendamento/', views.processa_agendamento, name='processa_agendamento')
]