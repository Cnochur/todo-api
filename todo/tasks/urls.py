from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.get_tasks, name='tasks'),
    path('add/', views.add_task, name='add_task'),
]