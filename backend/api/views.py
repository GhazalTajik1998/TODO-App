from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView

from .serializers import UserSerializer, TaskSerializer
from .permissions import IsAuthorPermission

from todo.models import Task
# Create your views here.

class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class TaskApiView(ListAPIView):
    permission_classes = [IsAuthorPermission]
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        tasks = Task.objects.filter(user=user)
        return tasks




