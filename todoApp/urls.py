from django.shortcuts import render
from django.urls import path
from .views import showDashboard

urlpatterns = [
    path('', showDashboard, name='showDashboard'),
]
