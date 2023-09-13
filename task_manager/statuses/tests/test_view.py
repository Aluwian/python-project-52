from django.urls import reverse_lazy
from .files import DownloadStatuses
from task_manager.statuses.models import Status


class TestStatusList(DownloadStatuses):
    def test_statuses_view(self):
        response = self.client.get(reverse_lazy("StatusesList"))
        self.assertEqual(response.status_code, 200)

    def test_statuses_content(self):
        response = self.client.get(reverse_lazy("StatusesList"))
        self.assertQuerysetEqual(
            response.context["statuses"], self.statuses, ordered=False
        )

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("StatusesList"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("Login"))


class TestCreateStatus(DownloadStatuses):
    def test_create_view(self):
        response = self.client.get(reverse_lazy("CreateStatus"))
        self.assertEqual(response.status_code, 200)

    def test_user_create(self):
        valid_data = self.new_status["create"]["valid"].copy()

        status = Status.objects.create(
            name=valid_data["name"], date_created=valid_data["date_created"]
        )
        self.assertEqual(status.name, valid_data["name"])

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("CreateStatus"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("Login"))