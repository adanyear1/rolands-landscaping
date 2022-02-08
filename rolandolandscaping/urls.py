"""
Definition of urls for rolandolandscaping.
"""

from datetime import datetime
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('estimate/', views.estimate, name='estimate'),
    path('gallery/', views.gallery, name='gallery'),
    path('projects/', views.projects, name='projects'),
    path('tree/', views.tree, name='tree'),
    path('concrete/', views.concrete, name='concrete'),
    path('zeroscaping/', views.zeroscaping, name='zeroscaping')
]