from django.urls import path
from task_manager.tasks.views import (
    TasksListView,
    CreateTaskView,
    # UpdateTaskView,
    # DeleteTaskView,
    # TaskView,
)


urlpatterns = [
    path("", TasksListView.as_view(), name="TasksList"),
    path("create/", CreateTaskView.as_view(), name="CreateTask"),
    # path("<int:pk>/update", UpdateTaskView.as_view(), name="UpdateTask"),
    # path("<int:pk>/delete/", DeleteTaskView.as_view(), name="DeleteTask"),
    # path("<int:pk>/", TaskView.as_view(), name="TaskPage"),
]
