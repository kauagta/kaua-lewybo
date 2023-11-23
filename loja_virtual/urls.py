from django import views
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
   
   
    path('preços/', views.preços, name='preços'),
    path('descrição/',views.descrição, name='descrição'),
]