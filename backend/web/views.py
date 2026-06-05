from django.shortcuts import render
from tasksAPI.models import Task


def index(request):
    new_tasks = Task.objects.filter(status="NEW")
    in_progress_tasks = Task.objects.filter(status="IN_PROGRESS")
    completed_tasks = Task.objects.filter(status="COMPLETE")
    context = {
        "new_tasks": new_tasks,
        "in_progress_tasks": in_progress_tasks,
        "completed_tasks": completed_tasks,
    }
    return render(request, 'web/index.html', context)
