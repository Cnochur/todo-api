from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PATCH'])
def update_task_status(request):
    task_id = int(request.data['id'])
    task = Task.objects.get(id=task_id)
    task.status = request.data['status']
    task.save()
    return Response({'success': "status has been updated"})

@api_view(['PUT'])
def edit_task(request):
    task_id = int(request.data['id'])
    task = Task.objects.get(id=task_id)
    task.title = request.data['title']
    task.description = request.data['description']
    task.save()
    return Response({'id': task.id + "updated"})

@api_view(['POST'])
def delete_task(request):
    task_id = int(request.data['id'])
    task = Task.objects.get(id=task_id)
    task.delete()
    return Response({'success': "deleted"})


