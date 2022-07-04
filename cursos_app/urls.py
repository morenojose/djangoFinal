from django.contrib import admin
from django.urls import path
from . import views



urlpatterns= [
path("cursos/", views.alumnos, name="cursos"),
path("", views.inicio , name="index"),

]