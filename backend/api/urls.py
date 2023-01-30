from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet,TaskViewSet

name = "api"
router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    # path("users/", UserApiView.as_view(), name="api_user"),
    path('', include(router.urls)),
    # path("tasks/", TaskApiView.as_view(), name='tasks'),
    # path("task/<int:id>", TaskDetailApiView.as_view(), name='detail')
]
