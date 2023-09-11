from django.test import TestCase, Client
from task_manager.helpers import open_file
from task_manager.statuses.models import Status


class DownloadStatuses(TestCase):
    fixtures = ["users.json", "statuses.json"]
    new_user = open_file("new_status.json")

    def SetUp(self):
        self.client = Client()
        self.status_1 = Status.objects.get(pk=1)
        self.status_2 = Status.objects.get(pk=2)
        self.status_3 = Status.objects.get(pk=3)
        self.count = Status.objects.count()
        self.statuses = Status.objects.all()
