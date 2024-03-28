from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView
from django.views.decorators.http import require_http_methods


from .models import Task

# Create your views here.

class TaskListView(ListView):
    model = Task

@require_http_methods(['POST'])
def add_task(request):
    task=request.POST.get('task')
    todo=Task.objects.create(task=task)
    todo.save()
    return redirect('home')


# class TaskDeleteView(DeleteView):
#     model = Task
#     success_url = reverse_lazy('home')

def delete_task(request,id):
    todo=Task.objects.get(pk=id)
    todo.delete()
    return redirect('home')


def update_status(request,id):
    todo=Task.objects.get(pk=id)
    todo.task_status= not todo.task_status
    todo.save()
    return redirect('home')


