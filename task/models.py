from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    title = models.CharField(max_length=255)
    initial = models.IntegerField(default=0)
    target = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)