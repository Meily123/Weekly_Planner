from django.contrib import admin
from django.urls import path
from .views import cobaTemplate, CreateWeeklyTask, ListViewWeeklyTask, DeleteViewWeeklyPlanner, DetailWeeklyTask, UpdateWeeklyTask

urlpatterns = [
    path('', ListViewWeeklyTask.as_view(), name='list'),
    path('create', CreateWeeklyTask.as_view(), name='create'),
    path('delete/<int:pk>', DeleteViewWeeklyPlanner.as_view(), name='delete'),
    path('detail/<int:pk>', DetailWeeklyTask.as_view(), name='detail'),
    path('update/<int:pk>', UpdateWeeklyTask.as_view(), name='update'),
    path('coba/', cobaTemplate.as_view())
]