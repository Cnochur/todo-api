from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.get_tasks, name='tasks'),
    path('add/', views.add_task, name='add_task'),
    path('edit-task/', views.edit_task, name='edit_task'),
    path('update-status/', views.update_task_status, name='update_status'),
    path('delete/', views.delete_task, name='delete_task'),

]