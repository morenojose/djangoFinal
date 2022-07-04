from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns= [
path("login", views.login_request, name="Login"),
path("register", views.register, name="Register"),
path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
path("editarPerfil", views.editarPerfil, name="editarPerfil"),
]

