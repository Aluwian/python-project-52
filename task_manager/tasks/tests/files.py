from django.test import TestCase, Client
from task_manager.helpers import open_file
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.tasks.models import Task
from task_manager.labels.models import Label


class DownloadTasks(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json", "labels.json"]
    new_task = open_file("new_task.json")

    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.client.force_login(self.user1)

        self.task_1 = Task.objects.get(pk=1)
        self.task_2 = Task.objects.get(pk=2)
        self.task_3 = Task.objects.get(pk=3)

        self.tasks = Task.objects.all()
        self.count = Task.objects.count()
