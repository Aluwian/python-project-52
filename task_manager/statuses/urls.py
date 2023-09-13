from django.urls import path
from task_manager.statuses.views import StatusListView, CreateStatusView


urlpatterns = [
    path("", StatusListView.as_view(), name="StatusesList"),
    path("create/", CreateStatusView.as_view(), name="CreateStatus"),
]
