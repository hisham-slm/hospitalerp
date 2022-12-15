from django.shortcuts import render

# Create your views here.

def fb (request):
    return render(request, 'fb_templates/fb_login.html')