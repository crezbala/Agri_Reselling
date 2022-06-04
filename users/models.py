from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django_mysql.models import ListCharField

class CustomUserManager(UserManager):
    pass
    


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    usertype=models.CharField(max_length=30)
    brandname=models.CharField(max_length=50,blank=True)
    Voted_spaces=ListCharField(base_field=models.IntegerField(),default=[],blank=True,null=True,size=100,max_length=100)