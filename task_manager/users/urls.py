from django.urls import path
from task_manager.users.views import UsersListView, CreateUserView


urlpatterns = [
    path("", UsersListView.as_view(), name="UsersList"),
    path("create/", CreateUserView.as_view(), name="CreateUser"),
]
