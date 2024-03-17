from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework  import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated

class TaskListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = TaskSerializer
    
    queryset = Task.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'priority']
    
    
class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "pk"