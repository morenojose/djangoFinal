from django.http import HttpResponse
from django.shortcuts import render
from  django.template import Template, Context


def home(request):
     return HttpResponse("<h1> home </h1>")

