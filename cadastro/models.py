from django.db import models
from login.models import Login

class Cadastro(models.Model):
    cad_codigo = models.IntegerField(primary_key=True, editable=False)
    cad_nome = models.CharField(max_length=30)
    cad_email = models.CharField(max_length=25, unique=True)
    cad_rua = models.CharField(max_length=25)
    cad_numero = models.CharField(max_length=10)
    cad_bairro = models.CharField(max_length=25)
    cad_cidade = models.CharField(max_length=25)
    cad_contato = models.CharField(max_length=20)
    cad_senha = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.cad_nome
    
class LoginCadastro(models.Model):
    lc_codigo = models.IntegerField(primary_key=True, editable=False)
    log_codigo = models.ForeignKey(Login, on_delete=models.PROTECT)
    cad_codigo = models.ForeignKey(Cadastro, on_delete=models.PROTECT)
