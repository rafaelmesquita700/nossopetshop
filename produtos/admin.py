from django.contrib import admin
from .models import Produtos

# Register your models here.
@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('pro_codigo','pro_nome', 'pro_valor', 'pro_qtde', 'pro_tipo')
    list_filter = ('pro_codigo', 'pro_nome', 'pro_valor', 'pro_qtde', 'pro_tipo')
    list_editable = ('pro_nome', 'pro_valor', 'pro_qtde', 'pro_tipo')
    search_fields = ('pro_codigo','pro_nome', 'pro_valor', 'pro_qtde', 'pro_tipo')