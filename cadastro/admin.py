from django.contrib import admin
from .models import Cadastro

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('cad_nome', 'cad_email', 'cad_rua', 'cad_numero', 'cad_bairro', 'cad_cidade', 'cad_contato')
    list_filter = ('cad_nome', 'cad_email', 'cad_rua', 'cad_numero', 'cad_bairro', 'cad_cidade', 'cad_contato')
    list_editable = ('cad_email', 'cad_rua', 'cad_numero', 'cad_bairro', 'cad_cidade', 'cad_contato')
    search_fields = ('cad_nome', 'cad_email', 'cad_rua', 'cad_numero', 'cad_bairro', 'cad_cidade', 'cad_contato')