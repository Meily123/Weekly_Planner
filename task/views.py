from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, View
from task.models import Task
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse

class cobaTemplate(TemplateView):
    template_name = 'test.html'


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
        for i in allTask:
            date[i.date.weekday()].append(i)
        context = {
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

            


