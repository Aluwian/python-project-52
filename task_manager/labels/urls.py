from django.urls import path
from task_manager.labels.views import (
    LabelListView,
    # CreateLabelView,
    # UpdateLabelView,
    # DeleteLabelView,
)

urlpatterns = [
    path("", LabelListView.as_view(), name="LabelsList"),
    # path("create/", CreateStatusView.as_view(), name="CreateStatus"),
    # path("<int:pk>/update", UpdateStatusView.as_view(), name="UpdateStatus"),
    # path("<int:pk>/delete/", DeleteStatusView.as_view(), name="DeleteStatus"),
]