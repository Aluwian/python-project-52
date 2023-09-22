from django.urls import path
from task_manager.statuses.views import (
    StatusListView,
    CreateStatusView,
    UpdateStatusView,
    DeleteStatusView,
)


urlpatterns = [
    path("", StatusListView.as_view(), name="StatusesList"),
    path("create/", CreateStatusView.as_view(), name="CreateStatus"),
    path("<int:pk>/update", UpdateStatusView.as_view(), name="UpdateStatus"),
    path("<int:pk>/delete/", DeleteStatusView.as_view(), name="DeleteStatus"),
]
