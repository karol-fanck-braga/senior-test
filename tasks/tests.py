from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task1 = Task.objects.create(title="Task 1", description='', status="in_progress", priority="1")
        self.task2 = Task.objects.create(title="Task 2", description='', status="done", priority="3")

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer' + token)

    def test_list_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_task(self):
        data = {'title': 'New Task', 'description': '', 'status': 'in_progress', 'priority': '2'}
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)

    def test_retrieve_task(self):
        response = self.client.get('/api/tasks/{self.task1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = TaskSerializer(self.task1)
        self.assertEqual(response.data, serializer.data)

    def test_update_task(self):
        data = {'title': 'Updated Task', 'status': 'done', 'priority': '1'}
        response = self.client.put('/api/tasks/{self.task1.pk}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Task')
        self.assertEqual(self.task1.status, 'done')
        self.assertEqual(self.task1.priority, '1')

    def test_delete_task(self):
        response = self.client.delete('/api/tasks/{self.task1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)
