from django.test import TestCase
from django.test.client import Client
from django.urls import reverse_lazy

from task_manager.users.models import User


class HomeTestFile(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = {"username": "test_user", "password": "test_pa11word"}
        self.user = User.objects.create_user(**self.test_user)


class MainPage(HomeTestFile):
    def test_main_page(self):
        response = self.client.get(reverse_lazy("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/users/")
        self.assertNotContains(response, "/statuses/")


class TestLoginUser(HomeTestFile):
    def test_login_view(self):
        response = self.client.get(reverse_lazy("login"))
        self.assertEqual(response.status_code, 200)


class TestLogoutUser(HomeTestFile):
    def test_logout_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy("logout"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse_lazy("home"))
