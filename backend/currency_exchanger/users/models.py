from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="info")
    phone = models.CharField(max_length=50)
    billing_address = models.CharField(max_length=200)

    def __str__(self):
        return self.user
