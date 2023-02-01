from rest_framework import serializers
from django.contrib.auth.models import User

from todo.models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
    

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('user',)
    

    # # Not working because my updated field is set to editable=False and my serializer
    # # does not contain the updated and created field
    
    # def validate_deadline(self, value):
    #     print(self.initial_data.get('updated'))
    #     if value <= self.initial_data.get('updated'):
    #         raise serializers.ValidationError("Deadline cannot be earlier that update time")
    #     return value
class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Task
        exclude = ('user',)
    
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "GET":
            fields['user'] = UserSerializer(read_only=True)
        return fields