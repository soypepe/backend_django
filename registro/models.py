from django.db import models

class Cliente(models.Model):
  nombre = models.CharField(max_length=100)
  direccion = models.CharField(max_length=100)
  telefono = models.CharField(max_length=20)
  ci = models.CharField(max_length=40)
  fecha = models.CharField(max_length=20, default='')
  edad = models.PositiveIntegerField(range(16,80), default=0)
  sexo = models.CharField(max_length=30, default='')