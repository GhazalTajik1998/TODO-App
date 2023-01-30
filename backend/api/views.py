from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import UserSerializer, TaskListSerializer, TaskCreateSerializer, TaskSerializer
# from .permissions import IsAuthorPermission



from todo.models import Task

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__username']
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TaskListSerializer
        else:
            return TaskCreateSerializer




