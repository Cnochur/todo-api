from django.shortcuts import render
from tasks.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'web/index.html', {"tasks": tasks})
