from django.db import models
from django.utils import timezone


class Clientes(models.Model):
    rubro = models.CharField(max_length=30)
    nombre = models.CharField(max_length=40)
    domicilio = models.CharField(max_length=50)


    class Meta:
        verbose_name = 'Clientes'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.rubro}, {self.nombre}'

class Contacto(models.Model):
    nombre=models.CharField(max_length=60)
    email=models.EmailField(max_length=250)
    mensaje=models.TextField(max_length=300)
