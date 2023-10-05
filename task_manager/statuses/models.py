from django.db import models
from django.urls import reverse_lazy


# Create your models her
class Status(models.Model):
    name = models.CharField(max_length=75, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("statuses")
