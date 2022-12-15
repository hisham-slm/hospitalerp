from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def index(request):
    # return HttpResponse("Welcome to Doctor's Page")


def index(request):
    return render(request,"doctor_templates/doctor.html")


def doctor_login(request):
    return render(request,"doctor_templates/login.html")
    

def doctor_signup(request):
    return render(request, "doctor_templates/signup.html")