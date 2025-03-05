from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', search_subject, name='search_subject'),
]