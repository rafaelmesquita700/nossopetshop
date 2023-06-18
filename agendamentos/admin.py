from django.contrib import admin
from .models import Agendamentos

# Register your models here.
@admin.register(Agendamentos)
class AgedamentosAdmin(admin.ModelAdmin):
    list_display = ('age_codigo',)