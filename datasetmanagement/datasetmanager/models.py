from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser

# Create your models here.
# class DatasetUser(models.Model):
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if username == '':
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False) # a superuser
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username

"""
class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.email
"""

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


