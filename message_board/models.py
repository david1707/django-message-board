from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, blank=False, unique=True)
    country = models.CharField(max_length=50, blank=False, null=False)
    joined_at = models.DateTimeField(auto_now_add=True)
    last_login_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
