from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, TaskListSerializer, TaskCreateSerializer, TaskSerializer
# from .permissions import IsAuthorPermission



from todo.models import Task
# Create your views here.

class UserApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class TaskApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateSerializer
        return TaskListSerializer

    def get_queryset(self):
        user = self.request.user
        tasks = Task.objects.filter(user=user)
        return tasks

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        tasks = Task.objects.filter(user=user)
        return tasks







