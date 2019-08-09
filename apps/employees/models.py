import os
from django.contrib.auth.models import AbstractUser
from django.db import models


def file_upload_path(instance, filename=''):
    return os.path.join('user', str(instance.id), filename)


# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to=file_upload_path, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}" if self.first_name else self.last_name or self.username
