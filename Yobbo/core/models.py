from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from ckeditor.fields import RichTextField

from django.utils import timezone

from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class YobboAdminManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Make sure to include the 'username' field in create_superuser
        extra_fields.setdefault('username', email)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, name, password, **extra_fields)


class YobboAdmin(AbstractUser):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=25, default = name )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']
    
    objects = YobboAdminManager()

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(YobboAdmin, on_delete=models.CASCADE, related_name='authored_posts')
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)
    likes = models.ManyToManyField(YobboAdmin, related_name='liked_posts')

    def __str__(self):
        return self.title
