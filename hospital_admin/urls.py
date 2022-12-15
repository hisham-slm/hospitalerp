from django.urls import path
from . import views


app_name='hadmin'


urlpatterns =[
    path('', views.admin_index, name='index'),
    path('login/', views.admin_login, name='log_in'),
    path('signup/' ,views.admin_signup, name='signup')
]