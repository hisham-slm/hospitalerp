from django.urls import path
from . import views


app_name='fb'

urlpatterns = [
    path('fb', views.fb, name='fb_login')
]