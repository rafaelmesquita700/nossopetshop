from django.db import models
from login.models import Login

# Create your models here.
class Produtos(models.Model):
    pro_codigo = models.IntegerField(primary_key=True, editable=False)
    pro_valor = models.DecimalField(max_digits=5, decimal_places=2)
    pro_nome = models.CharField(max_length=25)
    pro_tipo = models.CharField(max_length=25)
    pro_qtde = models.IntegerField()

    def __str__(self) -> str:
        return self.pro_nome

class Login_Produto(models.Model):
    lp_codigo = models.IntegerField(primary_key=True, editable=False)
    log_codigo = models.ForeignKey(Login, on_delete=models.PROTECT)
    pro_codigo = models.ForeignKey(Produtos, on_delete=models.PROTECT)