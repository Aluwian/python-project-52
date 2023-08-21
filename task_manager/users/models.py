from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __int__(self):
        full_name = self.get_full_name()
