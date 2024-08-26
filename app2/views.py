from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>soy el index de la app2</h1")
def texto(request):
    return HttpResponse("<h1>soy el texto</h1")