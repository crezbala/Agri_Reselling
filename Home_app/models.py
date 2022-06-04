from django.db import models
from users.models import CustomUser
from django_mysql.models import ListCharField
from django.db.models import CharField
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models



class prof(models.Model):
    did=models.AutoField(primary_key=True)
    userName = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.CharField(max_length=200, null=True,default="Check")
    password = models.CharField(max_length=200, null=True,default="Check")


    def __str__(self):
        return str(self.user)

