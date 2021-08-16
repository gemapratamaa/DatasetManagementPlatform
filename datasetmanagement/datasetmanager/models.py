from django.db import models

# Create your models here.
class DatasetUser(models.Model):
    name = models.CharField(max_length=30)

class Task(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        'DatasetUser',
        on_delete=models.CASCADE,
    )