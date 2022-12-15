from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def patient_signup(request):
    return render(request, 'patient_tempates/patient_signup.html')

def patient_home(request):
    return render(request, 'patient_tempates/patient_home.html')

def patient_login(request):
    return render(request, 'patient_tempates/patient_login.html')