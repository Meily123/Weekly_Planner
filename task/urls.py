from django.contrib import admin
from django.urls import path
from .views import cobaTemplate, CreateWeeklyTask, ListViewWeeklyTask, DeleteView

urlpatterns = [
    path('', ListViewWeeklyTask.as_view()),
    path('create', CreateWeeklyTask.as_view(), name='create'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete')
]