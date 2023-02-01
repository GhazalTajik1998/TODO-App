from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import UserSerializer, TaskListSerializer, TaskCreateSerializer, TaskSerializer
from .permissions import IsAuthorOfReadOnly



from todo.models import Task

class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthorOfReadOnly,IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied(" You can not perform this")
        serializer.save()

class TaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['priority', 'compeleted']
    filterset_fields = ['completed']
    ordering = ['completed', 'priority']
    def get_queryset(self):
        user = self.request.user
        if user is not None:    
            queryset = Task.objects.filter(user=user)
        return queryset

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TaskListSerializer
        else:
            return TaskCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)



