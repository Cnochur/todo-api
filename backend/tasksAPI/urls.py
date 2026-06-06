from . import views
from django.urls import path

app_name = 'tasksAPI'

urlpatterns = [
    path('', views.get_tasks, name='tasks'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('update/<int:task_id>/', views.update_task_status, name='update_status'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]