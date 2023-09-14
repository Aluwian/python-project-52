from django.db import models

from task_manager.statuses.models import Status
from task_manager.users.models import User


# Create your models here.
class Task(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
    )
    description = models.TextField(
        max_length=1000,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=False)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    # tags = models.CharField
