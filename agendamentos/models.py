from django.db import models
from login.models import Login

class Agendamentos(models.Model):
    age_codigo = models.IntegerField(primary_key=True, editable=False)

class LoginAgendamento(models.Model):
    la_codigo = models.IntegerField(primary_key=True, editable=False)
    log_codigo = models.ForeignKey(Login, on_delete=models.PROTECT)
    age_codigo = models.ForeignKey(Agendamentos, on_delete=models.PROTECT)