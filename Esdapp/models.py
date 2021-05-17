from django.db import models

# Create your models here.
class Esd(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField()
    setor = models.CharField(max_length=100)


    