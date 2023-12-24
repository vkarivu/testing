from django.shortcuts import render, redirect

from .models import Task
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, this is the index view of your Django app.")

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/task_list.html', {'tasks': tasks})



def task_detail(request, task_id):
    # Your view logic here
    return HttpResponse(f'Task Detail View for Task ID: {task_id}')


def task_input(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        created_at = request.POST['created_at']
        
        Task.objects.create(title=title, description=description, created_at=created_at)
        return redirect('task_input')  # Redirect to the task list page after data submission
    return render(request, 'myapp/task_input.html')