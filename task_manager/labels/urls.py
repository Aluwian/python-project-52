from django.urls import path
from task_manager.labels.views import (
    LabelListView,
    CreateLabelView,
    UpdateLabelView,
    DeleteLabelView,
)

urlpatterns = [
    path("", LabelListView.as_view(), name="LabelsList"),
    path("create/", CreateLabelView.as_view(), name="CreateLabel"),
    path("<int:pk>/update", UpdateLabelView.as_view(), name="UpdateLabel"),
    path("<int:pk>/delete/", DeleteLabelView.as_view(), name="DeleteLabel"),
]
