from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
path('', views.home, name='Home'),
path('contact', views.contact, name='Home'),
path('about', views.about, name='Home'),
]