from django.db import models
from django.utils import timezone

class Professor(models.Model):
    nome = models.CharField(max_length=80)
    telefone = models.IntegerField()
    email = models.EmailField()
    dataNascimento = models.DateField()
    cpf = models.BigIntegerField()

    def __str__(self):
        return self.nome    





# Create your models here.
