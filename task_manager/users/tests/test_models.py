from django.test import TestCase
from task_manager.users.models import User


class ModelsTestCase(TestCase):
    fixtures = ["users.json"]

    @classmethod
    def setUp(cls):
        cls.user_1 = User.objects.create(pk=2)
        cls.user_2 = User.objects.create(pk=3)
        cls.user_3 = User.objects.create(pk=4)

    def test_user_parameters(self):
        self.count = User.objects.count()
        self.assertEqual(self.count, 4)
