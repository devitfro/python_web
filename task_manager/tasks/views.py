from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        Task.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date')
        )
        return redirect('/tasks/')

    return render(request, 'tasks/add_task.html')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/tasks/')