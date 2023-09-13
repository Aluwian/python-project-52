from django.db import models


# Create your models her
class Status(models.Model):
    name = models.CharField(max_length=75, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
