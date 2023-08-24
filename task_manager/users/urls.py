from django.urls import path
from task_manager.users.views import (
    UsersListView,
    CreateUserView,
    UpdateUserView,
    DeleteUserView,
)


urlpatterns = [
    path("", UsersListView.as_view(), name="UsersList"),
    path("create/", CreateUserView.as_view(), name="CreateUser"),
    path("<int:pk>/update/", UpdateUserView.as_view(), name="UpdateUser"),
    path("<int:pk>/delete/", DeleteUserView.as_view(), name="DeleteUser"),
]
