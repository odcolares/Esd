from django.db import models

# Create your models here.
class esd(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    matricula = models.IntegerField()
    status = models.IntegerField()