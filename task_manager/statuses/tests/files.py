from django.test import TestCase, Client
from task_manager.helpers import open_file
from task_manager.statuses.models import Status
from task_manager.users.models import User


class DownloadStatuses(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json"]
    new_status = open_file("new_status.json")

    def setUp(self):
        self.client = Client()

        self.statuses = Status.objects.all()
        self.count = Status.objects.count()

        self.status_1 = Status.objects.get(pk=1)
        self.status_2 = Status.objects.get(pk=2)
        self.status_3 = Status.objects.get(pk=3)

        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)
