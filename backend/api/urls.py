from django.urls import path

from .views import UserApiView, TaskApiView, TaskDetailApiView

name = "api"

urlpatterns = [
    path("users/", UserApiView.as_view(), name="api_user"),
    path("tasks/", TaskApiView.as_view(), name='tasks'),
    path("task/<int:id>", TaskDetailApiView.as_view(), name='detail')
]
