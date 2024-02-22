from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import messages
# from home.models import User
from home.forms import Nameform

def register(request):
    if request.method=="POST":
        if(request.POST.get("submit")=="register"):
            username=request.POST.get("name")
            email=request.POST.get("email")
            password=request.POST.get("password")
            address=request.POST.get("address")
            # user=User(username=username,email=email,password=password,address=address)
            user=User(username=username,email=email,password=password)
            user.address=address  
            user.save()
            messages.success(request,"Registered successfully")
            return render(request,"login.html")
        else:
            return render(request,"login.html")
    # form=Nameform()
    # return render(request,"register.html",{"form":form})
    return render(request,"register.html")


def home(request):
    # if request.user.is_anonymous:
    #     print("user is anonymous")
    #     return redirect("register/")
    print("Hello home")
    return render(request,"index.html")

def login_user(request):
    if request.method=="POST":
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        # print(username,password)
        user = authenticate(request,username=username, password=password)
        if user is not None:
            print("login success")
            login(request,user)
            return redirect("/")
        else:
            messages.warning(request,"Invalid user")
            return redirect("login",)
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect("login")
