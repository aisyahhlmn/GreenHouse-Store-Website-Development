from django.shortcuts import render
from GreenHouse.models import SignIn, SignUp, Product, Cart;
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from asyncio import QueueFull
from django.db.models import Q

# Create your views here.

def registration(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Birth_Date=request.POST['Birth_Date']
        Email_Id=request.POST['Email_Id']
        Mobile_Number=request.POST['Mobile_Number']
        Gender=request.POST['Gender']
        Address=request.POST['Address']
        City=request.POST['City']
        Pin_Code=request.POST['Pin_Code']
        State=request.POST['State']
        Country = request.POST['Country']
        password = request.POST['password']
        retype_password = request.POST['retype_password']
        data=SignIn(Name=Name, Birth_Date=Birth_Date,Email_Id=Email_Id, Mobile_Number=Mobile_Number, Gender=Gender, Address=Address, 
        City=City, Pin_Code=Pin_Code, State=State, Country=Country, password=password, retype_password=retype_password)
        data.save()
        
        dict={
            'message' : 'YOUR INFORMATION HAS BEEN SAVED'
        }

        return render (request,"greenhouse/registration.html",dict)
    else:
        dict={
            'message' : ''
        }
        return render (request,"greenhouse/registration.html")

def login(request):
    users = SignUp.objects.filter(Q(Email_Id=request.GET.get('login')))
    return render(request, 'greenhouse/login.html',{'users':users})

def home(request):
    return render(request,"greenhouse/home.html")

def Product1(request):
    return render(request,"greenhouse/Product1.html")

def Product2(request):
    return render(request,"greenhouse/Product2.html")

def Product3(request):
    return render(request,"greenhouse/Product3.html")

def Product4(request):
    return render(request,"greenhouse/Product4.html")

def Product5(request):
    return render(request,"greenhouse/Product5.html")

#search and delete
def userprofile(request):
    User = SignIn.objects.filter(Q(Email_Id=request.GET.get('search')))
    return render(request, 'greenhouse/userprofile.html',{'User':User})

def deletedata(request,Email_Id):
    data = SignIn.objects.get(Email_Id=Email_Id)
    data.delete()
    return HttpResponseRedirect(reverse("userprofile"))

#update
def updatedata(request,ridename):
    User = SignIn.objects.get(Email_Id=Email_Id)
    dict={
        'User':User
    }       
    return render(request,"greenhouse/updatedata.html",dict)

def updates(request,ridename):
    Name=request.POST['Name']
    Birth_Date=request.POST['Birth_date']
    Email_Id=request.POST['Email_Id']
    Mobile_Number=request.POST['Mobile_Number']
    Gender=request.POST['Gender']
    Address=request.POST['Address']
    City=request.POST['City']
    Pin_Code=request.POST['Pin_Code']
    State=request.POST['State']
    Country=request.POST['Country']
    password=request.POST['password']

    data=User.objects.get(Email_Id=Email_Id)
    data.Name=Name
    data.Birth_Date=Birth_Date
    data.Email_Id=Email_Id
    data.Mobile_Number=Mobile_Number
    data.Gender=Gender
    data.Address=Address
    data.City=City
    data.Pin_Code=Pin_Code
    data.State=State
    data.Country=Country
    data.password=password    
    data.save()

    return HttpResponseRedirect(reverse("userprofile"))
