from . import views
from tasksAPI import views as task_views
from django.urls import path, include

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', include('tasksAPI.urls')),
]