from django.urls import reverse_lazy
from .files import DownloadLabels
from task_manager.labels.models import Label


class TestLabelsLict(DownloadLabels):
    def test_label_view(self):
        response = self.client.get(reverse_lazy("labels"))
        self.assertEqual(response.status_code, 200)

    def test_labels_content(self):
        response = self.client.get(reverse_lazy("labels"))
        self.assertQuerysetEqual(
            response.context["labels"], self.labels, ordered=False
        )

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("labels"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))


class TestCreateLabelView(DownloadLabels):
    def test_create_view(self):
        response = self.client.get(reverse_lazy("label_create"))
        self.assertEqual(response.status_code, 200)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("label_create"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_label_create(self):
        valid_data = self.new_label["create"]["valid"].copy()

        label = Label.objects.create(name=valid_data["name"])
        self.assertEqual(label.name, valid_data["name"])


class TestUpdateLabel(DownloadLabels):
    def test_update_view(self):
        response = self.client.get(reverse_lazy("label_update"))
        self.assertEqual(response.status_code, 200)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("label_update"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))


class TestDeleteLabel(DownloadLabels):
    def test_update_view(self):
        response = self.client.get(reverse_lazy("label_delete"))
        self.assertEqual(response.status_code, 200)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("label_delete"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))
