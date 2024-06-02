from django.urls import path
from django.contrib import admin
from . import views


app_name = "user"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.mylogin, name="login"),
    path('logout/', views.my_logout, name="logout"),
]