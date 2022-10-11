from django.shortcuts import render
from django.http import HttpResponse
# Create your views here,

def index(request):
    d = {
        "name": "Arun",
        "age" : 30
    }
    
    return HttpResponse("<b>Hello Worlds</b>")
