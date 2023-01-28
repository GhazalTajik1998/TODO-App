from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    # Charfield and TextField can not have NULL value in DB. 
    # It stores  '' string instead of null

    # Blank=True mean it is not required and the combo of Null and Blank come together.
    # When you can leave the field empty ( blank=True) then you should let it have null value

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    # Use auto_now_add at creation time , also it is recommended to not use them
    # Use your custom save method
    created = models.DateTimeField(editable=False)
    updated  = models.DateTimeField(editable=False)
    deadline = models.DateTimeField()
    priority = models.PositiveIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.id :
            self.created = timezone.now()
        
        self.updated = timezone.now()
        return super(Task, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title




