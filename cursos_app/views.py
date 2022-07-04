from django.shortcuts import render

# Create your views here.
def cursos(request):
    #show students
    return render(request, "cursos.html")

