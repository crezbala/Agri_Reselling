from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django_mysql.models import ListCharField

class CustomUserManager(UserManager):
    pass
    


class CustomUser(AbstractUser):
    objects = CustomUserManager()
