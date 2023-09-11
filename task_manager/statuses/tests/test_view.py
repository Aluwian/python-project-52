from django.urls import reverse_lazy
from .statuse_files import DownloadStatuses
from task_manager.statuses.models import Status


class TestStatusList(DownloadStatuses):
    def test_statuses_view(self):
        response = self.client.get(reverse_lazy("StatusesList"))
        self.assertEqual(response.status_code, 200)

    def test_statuses_content(self):
        response = self.client.get(reverse_lazy("StatusesList"))
        self.assertQuerysetEqual(response.context["statuses"], self.statuses)
