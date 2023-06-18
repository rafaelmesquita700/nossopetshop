from django.db import models
from agendamentos.models import Agendamentos

# Create your models here.
class Banhoetosa(models.Model):
    bet_codigo = models.IntegerField(primary_key=True, editable=False)
    bet_nomePet = models.CharField(max_length=15)
    bet_tipoPet = models.CharField(max_length=10)
    bet_raca = models.CharField(max_length=10, blank=True)
    bet_responsavel = models.CharField(max_length=25)
    bet_dia = models.DateField()
    bet_hora = models.TimeField()

    def __str__(self) -> str:
        return self.bet_nomePet

class Consultas(models.Model):
    con_codigo = models.IntegerField(primary_key=True, editable=False)
    con_nomePet = models.CharField(max_length=15)
    con_tipoPet = models.CharField(max_length=10)
    con_raca = models.CharField(max_length=10, blank=True)
    con_responsavel = models.CharField(max_length=25)
    con_dia = models.DateField()
    con_hora = models.TimeField()

    def __str__(self) -> str:
        return self.con_nomePet

class Adestramento(models.Model):
    ade_codigo = models.IntegerField(primary_key=True, editable=False)
    ade_nomePet = models.CharField(max_length=15)
    ade_tipoPet = models.CharField(max_length=10)
    ade_raca = models.CharField(max_length=10, blank=True)
    ade_responsavel = models.CharField(max_length=25)
    ade_dia = models.DateField()
    ade_hora = models.TimeField()

    def __str__(self) -> str:
        return self.ade_nomePet