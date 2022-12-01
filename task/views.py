from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, View, DetailView
from task.models import Task
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from task.form import TaskForm

class cobaTemplate(TemplateView):
    template_name = 'form_edit.html'


# Task CRUD
class CreateWeeklyTask(View):
    def post(self, request):
        try:
            Task.objects.create(
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
        allTask = Task.objects.all()
        date = [[],[],[],[],[],[],[]]
        cumulative_progress = 0
        max_weight = 1

        for i in allTask:
            max_weight = max(max_weight, i.weight)
        
        for i in allTask:
            cumulative_progress += int(i.initial)/int(i.target) * (i.weight/max_weight)
            date[i.date.weekday()].append(i)
        
        cumulative_progress /= max(1,allTask.count())
        

        context = {
            'score': round(cumulative_progress * 100, 2),
            'monday': date[0],
            'tuesday': date[1],
            'wednesday': date[2],
            'thursday': date[3],
            'friday': date[4],
            'saturday': date[5],
            'sunday': date[6]
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



