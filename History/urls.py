from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.getData, name = 'registered'),
   
    path("change-password/", views.change_password, name ="changepassword")
]

