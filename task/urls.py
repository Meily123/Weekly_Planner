from django.contrib import admin
from django.urls import path
from .views import CreateWeeklyTask, ListViewWeeklyTask, DeleteViewWeeklyPlanner, DetailWeeklyTask, UpdateWeeklyTask, customLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', ListViewWeeklyTask.as_view(), name='list'),
    path('create', CreateWeeklyTask.as_view(), name='create'),
    path('delete/<int:pk>', DeleteViewWeeklyPlanner.as_view(), name='delete'),
    path('detail/<int:pk>', DetailWeeklyTask.as_view(), name='detail'),
    path('update/<int:pk>', UpdateWeeklyTask.as_view(), name='update'),
    path('login/', customLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='task:login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
]