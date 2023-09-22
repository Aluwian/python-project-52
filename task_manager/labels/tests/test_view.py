from django.urls import reverse_lazy
from .files import DownloadLabels
from task_manager.labels.models import Label


class TestLabelsLict(DownloadLabels):
    def test_label_view(self):
        response = self.client.get(reverse_lazy("LabelsList"))
        self.assertEqual(response.status_code, 200)

    def test_labels_content(self):
        response = self.client.get(reverse_lazy("LabelsList"))
        self.assertQuerysetEqual(response.context["labels"], self.labels)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("LabelsList"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("Login"))


class TestCreateLabelView(DownloadLabels):
    def test_create_view(self):
        response = self.client.get(reverse_lazy("CreateLabel"))
        self.assertEqual(response.status_code, 200)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("CreateLabel"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("Login"))

    def test_label_create(self):
        valid_data = self.new_label["create"]["valid"].copy()

        label = Label.objects.create(
            name=valid_data["name"]
        )
        self.assertEqual(label.name, valid_data["name"])
