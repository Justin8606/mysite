"""from django.shortcuts import render
from django.http import HttpResponse

# Create your views here,

def index(request):
    return HttpResponse("hegfg hgfghfh")"""

from ast import Return
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import product

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

def products(request):
    #p = product.objects.filter(price__gt = 100000)
    p = product.objects.all()
    
    context = {'products':p}
    
    return render(request, 'myapp/products.html',context=context)

def product_details(request,id):
    p = product.objects.get(id=id)
    context = {'p':p}
    return render(request, 'myapp/product_details.html',context=context)

def add_product(request):
    p = product(name = "Samsung 32 Inch Monitor",price = 36000.0)
    p.description = "This is a Samsung Monitor"
    
    p.save()
    
    return HttpResponse(p)