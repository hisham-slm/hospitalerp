from django.urls import path
from . import views

app_name = 'doctor'


urlpatterns = [
    path('', views.index,name="index"),
    path('login', views.doctor_login,name="login"),
    path('signup', views.doctor_signup,name="signup")
    
]