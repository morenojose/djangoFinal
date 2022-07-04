from django.shortcuts import render
from operator import methodcaller
import py_compile
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from  django.template import Template, Context, loader
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from login_app.forms import  UserEditForm
from django.contrib.auth.models import User


# Create your views here.
def login_request(request):
    if request.method =="POST":
        form= AuthenticationForm(request , data=request.POST)
        if form.is_valid():
           usuario= form.cleaned_data.get("username")
           contra = form.cleaned_data.get("password")

           user= authenticate(username=usuario, password = contra)
           if user is not None:
            login(request,user)
            return render(request, "inicio.html", {"mensaje":f"bienvenido {usuario}"})
           else:
            return HttpResponse(f"usuario incorrecto")
        else:
         return HttpResponse(f"form incorrecto {form} ")

    form= AuthenticationForm()
    return render(request, "login.html", {"form":form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "usuario_registrado.html")
        else:
           return render(request, "registro.html", {"form":form})

    else:
        form = UserCreationForm()
        return render(request, "registro.html", {"form":form})



def editarPerfil(request):
    usuario= request.user
    if request.method=="POST":
        miFormulario= UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            usuario.email= informacion['email']
            password= informacion['password1']
            usuario.set_password= password
            usuario.save()

            return render(request , "inicio.html") 

    else:
        miFormulario= UserEditForm(initial={'email':usuario.email})
        return render(request, "editar_perfil.html", {"miFormulario":miFormulario , "usuario":usuario})










