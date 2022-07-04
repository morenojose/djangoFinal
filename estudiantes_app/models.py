import datetime
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse 


# Create your models here.
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    edad=models.IntegerField()
    telefono= models.IntegerField(default=00)
   
    def __str__(self):
        texto= "{0} {1} {2} {3}"
        return texto.format (self.name, self.address, self.edad, self.telefono)


    

class Cursos(models.Model):
    id = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=255)
    camada=models.IntegerField()

    def __str__(self):
        texto= "{0} {1} {2}"
        return texto.format (self.id, self.curso, self.camada)


class Docentes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    telefono =models.IntegerField()
    curso = models.CharField(max_length=255)

    def __str__(self):
        texto= "{0} {1} {2} {3}"
        return texto.format (self.id, self.nombre,  self.telefono, self.curso)


    

