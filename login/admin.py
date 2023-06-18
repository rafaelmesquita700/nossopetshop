from django.contrib import admin
from .models import Login

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('log_codigo', 'log_email')
    list_filter = ('log_codigo', 'log_email')
    list_editable = ('log_email',)
    search_fields = ('log_codigo', 'log_email')
    