from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.abt,name='about'),
    path('work',views.work,name='work'),
    path('contact',views.contact,name='contact')
]
