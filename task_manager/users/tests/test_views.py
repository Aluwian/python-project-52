from django.urls import reverse_lazy

from .files import DownloadUsers
from task_manager.users.models import User


class TestUserList(DownloadUsers):
    def test_list_view(self):
        response = self.client.get(reverse_lazy("UsersList"))
        self.assertEqual(response.status_code, 200)

    def test_users_content(self):
        response = self.client.get(reverse_lazy("UsersList"))
        self.assertQuerysetEqual(response.context["users"], self.users)


class TestCreateUser(DownloadUsers):
    def test_create_view(self):
        response = self.client.get(reverse_lazy("CreateUser"))
        self.assertEqual(response.status_code, 200)

    def test_user_create_valid(self):
        valid_data = self.new_user["create"]["valid"].copy()

        user = User.objects.create(
            username=valid_data["username"],
            first_name=valid_data["first_name"],
            last_name=valid_data["last_name"],
        )
        self.assertEqual(user.username, valid_data["username"])
        self.assertEqual(user.first_name, valid_data["first_name"])
        self.assertEqual(user.last_name, valid_data["last_name"])


class TestUpdateUser(DownloadUsers):
    def test_update_view(self):
        self.client.force_login(self.user_1)
        response = self.client.get(reverse_lazy("UpdateUser", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)

    def test_update_another_user(self):
        self.client.force_login(self.user_1)
        response = self.client.get(reverse_lazy("UpdateUser", kwargs={"pk": 2}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("UsersList"))

    def test_update_no_login(self):
        response = self.client.get(reverse_lazy("UpdateUser", kwargs={"pk": 2}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("Login"))


class TestDeleteUSer(DownloadUsers):
    def test_delete_view(self):
        self.client.force_login(self.user_1)
        response = self.client.get(reverse_lazy("DeleteUser", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)

    def test_delete_another_user(self):
        self.client.force_login(self.user_1)
        response = self.client.get(reverse_lazy("DeleteUser", kwargs={"pk": 2}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("UsersList"))

    def test_delete_no_login(self):
        response = self.client.get(reverse_lazy("DeleteUser", kwargs={"pk": 2}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("Login"))
