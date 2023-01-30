from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response

from .serializers import UserSerializer, TaskListSerializer, TaskCreateSerializer, TaskSerializer
# from .permissions import IsAuthorPermission



from todo.models import Task
# Create your views here.

# class UserApiView(ListCreateAPIView):
#     permission_classes = [IsAuthenticated]

#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class TaskApiView(ListCreateAPIView):
#     permission_classes = [IsAuthenticated]

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return TaskCreateSerializer
#         return TaskListSerializer

#     def get_queryset(self):
#         user = self.request.user
#         tasks = Task.objects.filter(user=user)
#         return tasks

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class TaskDetailApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskListSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'id'

#     def get_queryset(self):
#         user = self.request.user
#         tasks = Task.objects.filter(user=user)
#         return tasks
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TaskListSerializer
        else:
            return TaskCreateSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset 
# class TaskViewSet(ViewSet):
#     def list(self, request):
#         queryset = Task.objects.filter(user=request.user)
#         serializer = TaskListSerializer(queryset, many=True)
#         return Response(serializer.data)

    
    
#     def retrieve(self, request, pk=None):
#         queryset = Task.objects.all()
#         task = get_object_or_404(queryset, pk=pk)
#         serializer = TaskListSerializer(task)
        
#         return Response(serializer.data)



