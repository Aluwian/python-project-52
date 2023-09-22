from django.test import TestCase, Client
from task_manager.helpers import open_file
from task_manager.users.models import User


class DownloadUsers(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json", "labels.json"]
    new_user = open_file("new_user.json")

    def setUp(self):
        self.client = Client()
        self.user_1 = User.objects.get(pk=1)
        self.user_2 = User.objects.get(pk=2)
        self.user_3 = User.objects.get(pk=3)
        self.count = User.objects.count()
        self.users = User.objects.all()
