from django.shortcuts import render

# Create your views here.

# Create your views here.

def index(request):
    return render(request,"frontend/index.html")

def products(request):
    return render(request,"frontend/products.html")

def store(request):
    return render(request,"frontend/store.html")

def about(request):
    return render(request,"frontend/about.html")
    
