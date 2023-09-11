from django.urls import path
from task_manager.statuses.views import StatusListView


urlpatterns = [
    path("", StatusListView.as_view(), name="StatusesList"),
]
