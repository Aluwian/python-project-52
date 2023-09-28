from django.urls import path
from task_manager.users.views import (
    UsersListView,
    CreateUserView,
    UpdateUserView,
    DeleteUserView,
)


urlpatterns = [
    path("", UsersListView.as_view(), name="users"),
    path("create/", CreateUserView.as_view(), name="sign_up"),
    path("<int:pk>/update/", UpdateUserView.as_view(), name="user_update"),
    path("<int:pk>/delete/", DeleteUserView.as_view(), name="user_delete"),
]
