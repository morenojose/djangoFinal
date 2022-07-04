from django import forms


class Alumno_formulario (forms.Form):
    name = forms.CharField(max_length=40)
    address = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    telefono= forms.IntegerField()
   
class Curso_formulario (forms.Form):
    curso = forms.CharField(max_length=255)
    camada=forms.IntegerField()

class Docente_formulario (forms.Form):
    nombre = forms.CharField(max_length=255)
    telefono=forms.IntegerField()
    curso=forms.CharField(max_length=255)