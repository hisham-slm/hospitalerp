from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def admin_index(request):
    return render(request, 'admin_templates/admin_home.html')

def admin_login(request):
    return render(request, 'admin_templates/admin_login.html')

def admin_signup(request):
    return render(request, 'admin_templates/admin_signup.html')