from django.urls import path
from . import views

urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('categoria/', views.categorias, name='categorias'),
    path('compra/', views.compra, name='compra')
]