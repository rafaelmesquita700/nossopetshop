from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('validar_login/', views.validar_login, name='validar_login'),
    path('sair/', views.sair, name='sair')
]