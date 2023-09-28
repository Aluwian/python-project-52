from django.urls import path
from task_manager.labels.views import (
    LabelListView,
    CreateLabelView,
    UpdateLabelView,
    DeleteLabelView,
)

urlpatterns = [
    path("", LabelListView.as_view(), name="labels"),
    path("create/", CreateLabelView.as_view(), name="label_create"),
    path("<int:pk>/update", UpdateLabelView.as_view(), name="label_update"),
    path("<int:pk>/delete/", DeleteLabelView.as_view(), name="label_delete"),
]
