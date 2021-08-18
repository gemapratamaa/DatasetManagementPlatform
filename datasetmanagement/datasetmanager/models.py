from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.forms import ModelForm

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.CharField(
        verbose_name='email address',
        max_length=255,
        unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

class Task(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    file = models.FileField(
        upload_to='tasks/', 
        validators=[
            FileExtensionValidator(allowed_extensions=['zip'])
        ]
    )

    is_deleted = models.BooleanField(default=False)

class Dataset(models.Model):
    file_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    file = models.FileField(
        upload_to='',
        validators=[FileExtensionValidator(allowed_extensions=['zip'])]
    )
    uploader = models.ForeignKey(
        'User',
        to_field='email',
        #default='gemapratamaa@gmail.com', # ???
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)

class DatasetUploadForm(ModelForm):
    class Meta: 
        model = Dataset
        fields = ('file',)