from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.helloworld,name='index'),
    path('landing/',views.landing,name='landing'),
    path('download/',views.download_file,name='down'),
]