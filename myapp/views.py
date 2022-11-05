"""from django.shortcuts import render
from django.http import HttpResponse

# Create your views here,

def index(request):
    return HttpResponse("hegfg hgfghfh")"""

from ast import Return
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse

from myapp.models import product
from django.contrib.auth import authenticate, login

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
    # p = product(name = "Samsung 32 Inch Monitor",price = 36000.0)
    # p.description = "This is a Samsung Monitor"
    
    # p.save()
    if request.method == 'POST':
        name= request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        
        p = product(name=name,price=price,description=desc,image=image)
        p.save()
        
        return redirect('/myapp/products')
        
           
    return render(request,'myapp/add_product.html')

def update_product(request,id):
    p = product.objects.get(id=id)
    context = {'p':p}
    
    if request.method == 'POST':
        p.name= request.POST.get('name')
        p.price = request.POST.get('price')
        p.description = request.POST.get('desc')
        
        try:
            p.image = request.FILES['upload']
        except :
            pass
            
            
        # p = product(name=name,price=price,description=desc,image=image)
        p.save()
        
        return redirect('/myapp/products')
        
           
    return render(request,'myapp/update_product.html',context=context)

def delete_product(request,id):
    p = product.objects.get(id=id)
    context = {'p':p}
    
    if request.method == 'POST':
        p.delete()
        return redirect('/myapp/products')
        
           
    return render(request,'myapp/delete_product.html',context=context)