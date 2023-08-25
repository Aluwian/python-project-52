from django.test import TestCase
from django.test.client import Client
from django.urls import reverse_lazy


class MainPage(TestCase):
    client = Client()

    def test_main_page(self):
        response = self.client.get(reverse_lazy("Home"))
        self.assertEqual(response.status_code, 200)
