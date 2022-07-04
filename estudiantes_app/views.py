from operator import methodcaller
import py_compile
from django.http import HttpResponse
from django.shortcuts import redirect, render
from  django.template import Template, Context, loader
from django.views.generic import CreateView
from .models import Students, Cursos, Docentes
from .forms import Alumno_formulario , Curso_formulario, Docente_formulario
from login_app import views
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


# Create your views here.
def about(request):
    #show students
        return render(request, "nosotros.html")


def alumnos(request):
    #show students
    return HttpResponse("<h1> hola mundo </h1>")


def add_alumno(request):
    return HttpResponse("<h1> hola mundo </h1>")


def probar_template(request):

    datos={"nombre":"Jose","notas":[5,6,7]}
    plantilla= loader.get_template("template.html")
    documento= plantilla.render(datos)
    return HttpResponse(documento)

  
def inicio(request):
    return render(request, "index.html")

def students(request):
    #show students
    studentslist= Students.objects.all()
    return render(request, "students.html",{"students":studentslist})


def contact(request):
    #show students
    return render(request, "contact.html")

def cursos(request):
     cursos= Cursos.objects.all()
     return render(request, "cursos.html",{"cursos":cursos} )

def detalles_curso(request, id):
        curso= Cursos.objects.get(id = id)
        return render(request, "detalles_curso.html" , {"curso":curso})

class Add_student_view(CreateView):
    model=Students
    template_name= "add_student.html"
    fields="__all__"

def  alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario (request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            alumno= Students(name=datos["name"], address=datos["address"], edad= datos["edad"], telefono=datos["telefono"])
            alumno.save()
            return render (request, "formulario.html")
    return render (request, "formulario.html")



def buscar_alumno(request):
    return render(request, "buscar_alumno.html")


def busqueda_alumno(request):
    if request.GET["nombre"]:
        name= request.GET["nombre"]
        students= Students.objects.filter(name__icontains = name)
        return render(request, "resultado_busqueda_alumno.html" , {"students":students})
    else:
        return HttpResponse("Campo Vacio") 
    

def eliminar_alumno (request, id):
   alumno= Students.objects.get(id = id)
   alumno.delete()
   #volver al meno
   students= Students.objects.all()
   contexto={"students":students}
   return render(request, "students.html", contexto)


def edicion_alumno(request, id):
    alumno= Students.objects.get(id = id)
    if request.method == "POST":
         mi_formulario = Alumno_formulario (request.POST)
         if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            alumno.name=datos["name"]
            alumno.address=datos["address"] 
            alumno.edad= datos["edad"]
            alumno.telefono=datos["telefono"]
            alumno.save()
            students= Students.objects.all()
            contexto={"students":students}
            return render(request, "students.html", contexto)

            
    else:
        mi_formulario = Alumno_formulario (initial={"name":Students.name, "address":Students.address, "edad":Students.edad,"telefono":Students.telefono})
    
    return render (request, "edicion_alumno.html", {"mi_formulario": mi_formulario, "alumno":alumno })

class Alta_Curso(CreateView):
    model=Cursos
    template_name= "alta_curso.html"
    fields="__all__"
    
def  curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario (request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            curso= Cursos(curso=datos["curso"], camada=datos["camada"])
            curso.save()
            return render (request, "formulario_curso.html")
    return render (request, "formulario_curso.html")


def buscar_curso(request):
    return render(request, "buscar_curso.html")

def busqueda_curso(request):
    if request.GET["curso"]:
        curso_buscado= request.GET["curso"]
        curso= Cursos.objects.filter(curso__icontains = curso_buscado)
        return render(request, "resultado_busqueda_curso.html" , {"curso":curso})
    else:
        return HttpResponse("Campo Vacio") 


def eliminar_curso (request, id):
   curso= Cursos.objects.get(id = id)
   curso.delete()
   #volver al meno
   cursos= Cursos.objects.all()
   contexto={"cursos":cursos}
   return render(request, "cursos.html", contexto)

def edicion_curso(request, id):
    curso= Cursos.objects.get(id = id)
    if request.method == "POST":
         mi_formulario = Curso_formulario (request.POST)
         if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            curso.curso=datos["curso"]
            curso.camada=datos["camada"] 
            curso.save()
            cursos= Cursos.objects.all()
            contexto={"cursos":cursos}
            return render(request, "cursos.html", contexto)  
    else:
        mi_formulario = Curso_formulario (initial={"curso":Cursos.curso, "camda":Cursos.camada})
    
    return render (request, "edicion_curso.html", {"mi_formulario": mi_formulario, "curso":curso })




def docentes(request):
     docentes= Docentes.objects.all()
     return render(request, "docentes.html",{"docentes":docentes} )


class Alta_Docente(CreateView):
    model=Docentes
    template_name= "alta_docente.html"
    fields="__all__"
    
def  docente_formulario(request):
    if request.method == "POST":
        mi_formulario = Docente_formulario (request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            docente= Docentes(nombre=datos["nombre"], telefono=datos["telefono"],curso=datos["curso"])
            docente.save()
            return render (request, "formulario_docente.html")
    return render (request, "formulario_docente.html")


def buscar_docente(request):
    return render(request, "buscar_docente.html")

def busqueda_docente(request):
    if request.GET["nombre"]:
        docente_buscado= request.GET["nombre"]
        docente= Docentes.objects.filter(nombre__icontains = docente_buscado)
        return render(request, "resultado_busqueda_docente.html" , {"docente":docente})
    else:
        return HttpResponse("Campo Vacio") 


def eliminar_docente (request, id):
   docente= Docentes.objects.get(id = id)
   docente.delete()
   #volver al meno
   docentes= Docentes.objects.all()
   contexto={"docentes":docentes}
   return render(request, "docentes.html", contexto)

def edicion_docente(request, id):
    docente= Docentes.objects.get(id = id)
    if request.method == "POST":
         mi_formulario = Docente_formulario (request.POST)
         if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            docente.nombre=datos["nombre"]
            docente.telefono=datos["telefono"]
            docente.curso=datos["curso"] 
            docente.save()
            docentes= Docentes.objects.all()
            contexto={"docentes":docentes}
            return render(request, "docentes.html", contexto)  
    else:
        mi_formulario = Curso_formulario (initial={"nombre":Docentes.nombre, "telefono":Docentes.telefono, "curso":Docentes.curso})
    
    return render (request, "edicion_docente.html", {"mi_formulario": mi_formulario, "docente":docente })
