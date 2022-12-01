from django.contrib import admin
from django.urls import path
from .views import CreateWeeklyTask, ListViewWeeklyTask, DeleteViewWeeklyPlanner, DetailWeeklyTask, UpdateWeeklyTask, customLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ListViewWeeklyTask.as_view()), name='list'),
    path('create', login_required(CreateWeeklyTask.as_view()), name='create'),
    path('delete/<int:pk>', login_required(DeleteViewWeeklyPlanner.as_view()), name='delete'),
    path('detail/<int:pk>', login_required(DetailWeeklyTask.as_view()), name='detail'),
    path('update/<int:pk>', login_required(UpdateWeeklyTask.as_view()), name='update'),
    path('accounts/login/', customLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='task:login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
]