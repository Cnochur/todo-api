from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_task_status(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_task(request, task_id):
    try:
        task = Task.objects.get(id=int(task_id))
    except Task.DoesNotExist:
        return Response({'error': "Task id does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = TaskSerializer(instance=task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=int(task_id))
    except Task.DoesNotExist:
        return Response({'error': "Task id does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    task.delete()
    return Response({'success': "deleted"}, status=status.HTTP_200_OK)


