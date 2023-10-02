from django.urls import path
from task_manager.statuses.views import (
    StatusListView,
    CreateStatusView,
    UpdateStatusView,
    DeleteStatusView,
)


urlpatterns = [
    path("", StatusListView.as_view(), name="statuses"),
    path("create/", CreateStatusView.as_view(), name="status_create"),
    path("<int:pk>/update/", UpdateStatusView.as_view(), name="status_update"),
    path("<int:pk>/delete/", DeleteStatusView.as_view(), name="status_delete"),
]
