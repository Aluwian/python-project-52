from django.test import TestCase, Client
from task_manager.helpers import open_file
from task_manager.users.models import User
from task_manager.labels.models import Label


class DownloadLabels(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json", "labels.json"]
    new_label = open_file("new_label.json")

    def setUp(self):
        self.client = Client()

        self.labels = Label.objects.all()
        self.count = Label.objects.count()

        self.label_1 = Label.objects.get(pk=1)
        self.label_2 = Label.objects.get(pk=2)
        self.label_3 = Label.objects.get(pk=3)

        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)
