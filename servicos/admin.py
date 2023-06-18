from django.contrib import admin
from .models import Banhoetosa, Adestramento, Consultas

@admin.register(Banhoetosa)
class BanhoeTosaAdmin(admin.ModelAdmin):
    list_display = ('bet_codigo', 'bet_nomePet', 'bet_tipoPet', 'bet_raca', 'bet_responsavel', 'bet_dia', 'bet_hora')
    
@admin.register(Consultas)
class ConsultasAdmin(admin.ModelAdmin):
    list_display = ('con_codigo', 'con_nomePet', 'con_tipoPet', 'con_raca', 'con_responsavel', 'con_dia', 'con_hora')
    
@admin.register(Adestramento)
class AdestramentoAdmin(admin.ModelAdmin):
    list_display = ('ade_codigo', 'ade_nomePet', 'ade_tipoPet', 'ade_raca', 'ade_responsavel', 'ade_dia', 'ade_hora')

