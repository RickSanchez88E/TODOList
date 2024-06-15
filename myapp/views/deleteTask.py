from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import home_todolist_model
from myapp.forms import home_todolist


def delete_task(request, task_id):
    task = get_object_or_404(home_todolist_model, id=task_id)
    task.delete()
    return redirect('home')
