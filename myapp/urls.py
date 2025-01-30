from django.contrib import admin
from django.urls import path
from myapp.views import *
from . import views


urlpatterns = [
    path('',Front_page),
]