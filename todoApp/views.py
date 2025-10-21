from django.shortcuts import render
from entities.models import Task

# Create your views here.

def showDashboard(request):

    # Getting the model and database data available to the template
    task_list = Task.objects.all()
    context = {'task_list': task_list}

    return render(request, 'dashboard.html', context)