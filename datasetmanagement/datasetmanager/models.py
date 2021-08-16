from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
# class DatasetUser(models.Model):
class User(models.Model):
    name = models.CharField(max_length=30)

class Task(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    file = models.FileField(
        upload_to='tasks/', 
        validators=[FileExtensionValidator(allowed_extensions=['zip'])]
    )

class Dataset(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    file = models.FileField(
        upload_to='datasets/', 
        validators=[FileExtensionValidator(allowed_extensions=['zip'])]
    )