from django.db import models

# Create your models here.
class Task(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    initial = models.IntegerField(default=0)
    target = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)