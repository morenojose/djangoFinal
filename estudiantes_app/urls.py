from django.contrib import admin
from django.urls import path
from . import views
from login_app import urls
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required


urlpatterns= [
path("Nosotros", views.about,name="about"),
path("alumnos", views.alumnos),
path("alta_alumno", views.alumno_formulario, name="alta_alumno"),
path("template/", views.probar_template),
path("", views.inicio , name="index"),
path("students", views.students , name="students"),
path("contact", views.contact,name="contact"),
path("buscar_alumno", views.buscar_alumno, name= "buscar_alumno"),
path("busqueda_alumno", views.busqueda_alumno, name= "busqueda_alumno"),
path("eliminar_alumno/<id>", views.eliminar_alumno , name="eliminar_alumno"),
path("edicion_alumno/<int:id>", views.edicion_alumno ,name="edicion_alumno"),
path("edicion_alumno/", views.edicion_alumno ,name="edicion_alumno"),

path("cursos", views.cursos, name="Cursos"),
path("detalles_curso/<int:id>", views.detalles_curso, name="detalles_curso"),
path("alta_curso", views.curso_formulario, name="alta_curso"),
path("buscar_curso", views.buscar_curso, name= "buscar_curso"),
path("busqueda_curso", views.busqueda_curso, name= "busqueda_curso"),
path("edicion_curso/<int:id>", views.edicion_curso ,name="edicion_curso"),
path("edicion_curso/", views.edicion_curso ,name="edicion_curso"),
path("eliminar_curso/<id>", views.eliminar_curso , name="eliminar_curso"),


path("docentes", views.docentes, name="docentes"),
path("alta_docente", views.docente_formulario, name="alta_docente"),
path("buscar_docente", views.buscar_docente, name= "buscar_docente"),
path("busqueda_docente", views.busqueda_docente, name= "busqueda_docente"),
path("edicion_docente/<int:id>", views.edicion_docente ,name="edicion_docente"),
path("edicion_docente/", views.edicion_docente ,name="edicion_docente"),
path("eliminar_docente/<id>", views.eliminar_docente , name="eliminar_docente"),

]