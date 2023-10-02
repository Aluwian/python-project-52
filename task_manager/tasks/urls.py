from django.urls import path
from task_manager.tasks.views import (
    TasksListView,
    CreateTaskView,
    UpdateTaskView,
    DeleteTaskView,
    TaskView,
)


urlpatterns = [
    path("", TasksListView.as_view(), name="tasks"),
    path("create/", CreateTaskView.as_view(), name="task_create"),
    path("<int:pk>/update/", UpdateTaskView.as_view(), name="task_update"),
    path("<int:pk>/delete/", DeleteTaskView.as_view(), name="task_delete"),
    path("<int:pk>/", TaskView.as_view(), name="task_show"),
]
