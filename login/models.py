from django.db import models

class Login(models.Model):
    log_codigo = models.IntegerField(primary_key=True, editable=False)
    log_email = models.CharField(max_length=25)
    log_senha = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.log_email