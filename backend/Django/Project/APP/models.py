from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()