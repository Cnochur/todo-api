from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

# Create your tests here.

class TasksTest(APITestCase):

    def setUp(self):
        pass

    def test_task_creation(self):
        data = {'user_id':'1', 'title': 'Test Add Task', 'description': 'Test Add Task'}
        response = self.client.post('/tasks/add/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.get(id=1)
        self.assertEqual(task.title, 'Test Add Task')
        self.assertEqual(task.description, 'Test Add Task')
        self.assertEqual(task.user_id, 1)

    def test_task_list(self):
        Task.objects.create(user_id=1, title="Test Add Task", description="Test Add Task")
        response = self.client.get('/tasks/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.get(id=1)
        self.assertEqual(task.title, 'Test Add Task')
        self.assertEqual(task.description, 'Test Add Task')
        self.assertEqual(task.user_id, 1)

    def test_edit_task(self):
        task = Task.objects.create(user_id=1, title="Test Add Task", description="Test Add Task")
        data={'title': 'Test Edit Task', 'description': 'Test Edit Task'}
        response = self.client.put('/tasks/edit/1/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        task.refresh_from_db()

        self.assertEqual(task.title, 'Test Edit Task')
        self.assertEqual(task.description, 'Test Edit Task')
        self.assertEqual(task.user_id, 1)

    def test_delete_task(self):
        Task.objects.create(user_id=1, title="Test Add Task", description="Test Add Task")
        response = self.client.delete('/tasks/delete/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 0)

    def test_update_task_status(self):
        task = Task.objects.create(user_id=1, title="Test Add Task", description="Test Add Task")
        data={'status': 'COMPLETE'}
        response = self.client.patch('/tasks/update/1/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        task.refresh_from_db()

        self.assertEqual(task.status, 'COMPLETE')
        self.assertEqual(task.description, 'Test Add Task')
        self.assertEqual(task.user_id, 1)

