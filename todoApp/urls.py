from django.urls import path
from .views import showDashboard, task_create, task_complete, task_edit, task_delete

urlpatterns = [
    path('', showDashboard, name='showDashboard'),
    path('tasks/add/', task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', task_delete, name='task_delete'),
    path('task/<int:pk>/complete/', task_complete, name='task_complete'),
]

