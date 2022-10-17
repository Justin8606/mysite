"""from django.shortcuts import render
from django.http import HttpResponse

# Create your views here,

def index(request):
    return HttpResponse("hegfg hgfghfh")"""

from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here,

def index(request):
    d = {
        "name": "Arun",
        "age": 30,
    }
    
    li = ["Allen","sreerag","Alwin","Allu"]
    
    for i in range (0,10):
        print(i)
        
        context = {'names': li}
        
    
    return render(request, 'myapp/index.html',context=context)

def news_one(request):
    return render(request, 'listing/news_one.html')
