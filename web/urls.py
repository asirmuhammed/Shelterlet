from django.contrib import admin
from django.urls import path
from . import views


app_name = 'web'
urlpatterns = [
    path('',views.Index,name="index"),
    path('base',views.base,name="base"),
    path('about',views.About,name="about"),
    path('blog/<int:id>/',views.blog,name="blog"),
    path('services',views.Services,name="services"),
    path('properties',views.Properties,name="properties"),
    path('contact',views.contact,name="contact")
]
