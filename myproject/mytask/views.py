from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    return render(request,"index.html")

def creat_user(request):
    if request.method == 'POST':
        name=request.POST["name"]
        email=request.POST["email"]
        #password=request.POST["password"]
        password=make_password(request.POST["password"])
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exist")
        else:
            User.objects.create(name=name,email=email,password=password)
            return HttpResponse("User created successfully")
        
    
def data(request):
    user_obj=User.objects.all()
    return render(request,"table.html",{"user_obj":user_obj})

def delete_user(request,pk):
    User.objects.get(id=pk).delete()
    return redirect("/table/")

def update(request,uid):
    user_obj=User.objects.get(id=uid)
    return render(request,"update.html",{"user_obj":user_obj})

def update_user(request):
    if request.method=="POST":
        uid=request.POST.get("uid")
        name=request.POST.get("name")
        email=request.POST.get("email")
        User.objects.filter(id=uid).update(name=name,email=email)
        return redirect("/table/")