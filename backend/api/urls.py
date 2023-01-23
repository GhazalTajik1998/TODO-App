from django.urls import path

from .views import UserApiView, TaskApiView

name = "api"

urlpatterns = [
    path("users/", UserApiView.as_view(), name="api_user"),
    path("tasks/", TaskApiView.as_view(), name='tasks')
]
