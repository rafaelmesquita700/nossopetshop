from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('processa_cadastro/', views.processa_cadastro, name='processa_cadastro')
]