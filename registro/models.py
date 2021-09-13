from django.db import models

class Cliente(models.Model):
  nombre = models.CharField(max_length=100)
  direccion = models.CharField(max_length=100)
  telefono = models.CharField(max_length=100)
  ci = models.CharField(max_length=100)