from django.shortcuts import render, get_object_or_404, redirect
from entities.models import Task
from entities.forms import TaskForm

def showDashboard(request):

    # Get the sort parameters from the request
    if 'sort' in request.GET:
        sort = request.GET.get('sort')
    else:
        sort = '-priority'

    task_list = Task.objects.all().order_by(sort)


    context = {'task_list': task_list}
    return render(request, 'dashboard.html', context)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showDashboard')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form, 'action': 'Create'})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('showDashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form, 'action': 'Edit'})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('showDashboard')
    return render(request, 'task_confirm_delete.html', {'task': task})