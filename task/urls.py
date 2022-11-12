from django.contrib import admin
from django.urls import path
from .views import cobaTemplate

urlpatterns = [
    path('', cobaTemplate.as_view())
]