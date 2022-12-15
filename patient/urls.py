from django.urls import path
from . import views


app_name = 'patient'



urlpatterns = [
    path('patient/', views.patient_signup, name='patient_signup'),
    path('', views.patient_home, name='patient_home'),
    path('signup/', views.patient_login, name='patient_login')
]