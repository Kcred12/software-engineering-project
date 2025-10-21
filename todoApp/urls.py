from django.shortcuts import render
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
]
