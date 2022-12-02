from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, View, DetailView, FormView
from task.models import Task
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from task.form import TaskForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class customLoginView(LoginView):
    template_name = "login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('task:list')


# Task CRUD
class CreateWeeklyTask(View):
    def post(self, request):
        try:
            Task.objects.create(
                user=self.request.user,
                date=request.POST.get('date'),
                title=request.POST.get('title'),
                initial=request.POST.get('initial'),
                target=request.POST.get('target'),
                weight=request.POST.get('weight')
            )
            return JsonResponse({
                    'massage': 'success'
                }, status=200)
        except:
            return JsonResponse({
                'massage': 'Failed'
            }, status=400)


class ListViewWeeklyTask(View):
    def get(self, request):
        allTask = Task.objects.filter(user=self.request.user)
        date = [[],[],[],[],[],[],[]]
        cumulative_progress = 0
        max_weight = 1

        for i in allTask:
            max_weight = max(max_weight, i.weight)
        
        important = ''

        days = {
            0 : 'Monday',
            1 : 'Tuesday',
            2 : 'Wednesday',
            3 : 'Thrusday',
            4 : 'Friday',
            5 : 'Saturday',
            6 : 'Sunday'
        }

        max_bobot = 0
        
        for i in allTask:
            cumulative_progress += int(i.initial)/int(i.target) * (i.weight/max_weight)
            date[i.date.weekday()].append(i)
            if important == '':
                important = i
                max_bobot = i.weight
                important_progress = round(int(i.initial)/int(i.target)*100, 2)
                important_day = days[i.date.weekday()]
            if i.weight > max_bobot and (100 != round(int(i.initial)/int(i.target)*100, 2)):
                important = i
                max_bobot = i.weight
                important_progress = round(int(i.initial)/int(i.target)*100, 2)
                important_day = days[i.date.weekday()]
        
        cumulative_progress /= max(1,allTask.count())

        context = {
            'score': round(cumulative_progress * 100, 2),
            'monday': date[0],
            'tuesday': date[1],
            'wednesday': date[2],
            'thursday': date[3],
            'friday': date[4],
            'saturday': date[5],
            'sunday': date[6],
            'important_task': important,
            'important_progress' : important_progress,
            'important_day' : important_day
        }
        return render(request, 'test.html', context)


class DeleteViewWeeklyPlanner(DeleteView):
    model = Task
    success_url = reverse_lazy('task:list')


class DetailWeeklyTask(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        context = {
            'date' : task.date,
            'title' : task.title,
            'progress' : round(int(task.initial)/int(task.target) * 100, 2),
            'weight' : task.weight

        }
        return JsonResponse(context)


class UpdateWeeklyTask(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'form_edit.html'
    success_url = reverse_lazy('task:list')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task:list')

    def form_valid(self, form):
        print('form_valid')
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task:list')
        return super(RegisterPage, self).get(*args, **kwargs)

class grafikWeekly(View):
    def get(self, request):
        allTask = Task.objects.filter(user=self.request.user)
        date = [0,0,0,0,0,0,0]
        jumlah = [0,0,0,0,0,0,0]
        cumulative_progress = 0
        max_weight = 1

        for i in allTask:
            max_weight = max(max_weight, i.weight)
        
        for i in allTask:
            cumulative_progress += int(i.initial)/int(i.target) * (i.weight/max_weight)
            date[i.date.weekday()] += round(int(i.initial)/int(i.target)*100, 2)
            jumlah[i.date.weekday()] += 1
        


        context = {
            'monday': round(date[0]/max(1, jumlah[0]), 2),
            'tuesday': round(date[1]/max(1, jumlah[1]), 2),
            'wednesday': round(date[2]/max(1, jumlah[2]), 2),
            'thursday': round(date[3]/max(1, jumlah[3]),2),
            'friday': round(date[4]/max(1, jumlah[4]),2),
            'saturday': round(date[5]/max(1, jumlah[5]),2),
            'sunday': round(date[6]/max(1, jumlah[6]),2),
        }
        return render(request, 'grafik.html', context)


