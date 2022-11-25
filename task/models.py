from django.db import models

# Create your models here.
class Task(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    initial = models.IntegerField(null=True, blank=True)
    target = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(default=1)