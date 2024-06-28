from django.db import models

# Create your models here.

class Fotografia(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [titulo = {self.titulo}]"