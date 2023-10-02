from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label


# Create your models here
class Task(models.Model):
    name = models.CharField(
        max_length=150, blank=False, unique=True, verbose_name=_("Name")
    )
    description = models.TextField(
        max_length=1000, blank=True, verbose_name=_("Description")
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Creation date"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="author",
        blank=False,
        verbose_name=_("Author"),
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="statuses",
        blank=False,
        verbose_name=_("Status"),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="executor",
        blank=True,
        null=True,
        verbose_name=_("Executor"),
    )
    labels = models.ManyToManyField(
        Label,
        through="LabelDeleteProtection",
        through_fields=("task", "label"),
        related_name="labels",
        verbose_name=_("Labels"),
        blank=(True,),
    )

    def __str__(self):
        return self.name


class LabelDeleteProtection(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.PROTECT,
    )
