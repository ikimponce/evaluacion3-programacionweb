from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    apepat=models.CharField(max_length=30)
    apemat=models.CharField(max_length=30)
    edad=models.IntegerField(max_length=30)
    nombre_vacuna=models.CharField(max_length=50)
    fecha=models.DateField()