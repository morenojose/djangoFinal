from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import clear_script_prefix


class UserEditForm(UserCreationForm):

    email= forms.EmailField(label="modificar")
    password1= forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña" , widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['email' , 'password1', 'password2']
        help_texts= {k:"" for k in fields }


