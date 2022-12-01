from django.contrib import admin
from django.urls import path
from .views import cobaTemplate, CreateWeeklyTask, ListViewWeeklyTask, DeleteViewWeeklyPlanner

urlpatterns = [
    path('', ListViewWeeklyTask.as_view(), name='list'),
    path('create', CreateWeeklyTask.as_view(), name='create'),
    path('delete/<int:pk>', DeleteViewWeeklyPlanner.as_view(), name='delete')
]