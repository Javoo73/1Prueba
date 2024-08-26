from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>soy el index</h1")
def vista1(request):
    return HttpResponse("<h1>soy el vista1</h1")