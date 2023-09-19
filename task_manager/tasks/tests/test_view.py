from django.urls import reverse_lazy
from .files import DownloadTasks
from task_manager.tasks.models import Task


class TestTasksList(DownloadTasks):
    def test_tasks_view(self):
        response = self.client.get(reverse_lazy("TasksList"))
        self.assertEqual(response.status_code, 200)

    def test_tasks_content(self):
        response = self.client.get(reverse_lazy("TasksList"))
        self.assertQuerySetEqual(response.context["tasks"], self.tasks)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("TasksList"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("Login"))


class TestTaskView(DownloadTasks):
    def test_task_view(self):
        response = self.client.get(reverse_lazy("TaskPage", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("TaskPage", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("Login"))

    def test_task_content(self):
        response = self.client.get(reverse_lazy("TaskPage", kwargs={"pk": 1}))
        self.assertEqual(response.context["task"].name, self.task_1.name)
        self.assertEqual(response.context["task"].author, self.task_1.author)


class TestCreateTask(DownloadTasks):
    def test_create_view(self):
        response = self.client.get(reverse_lazy("CreateTask"))
        self.assertEqual(response.status_code, 200)

    def test_task_create(self):
        data = self.new_task["create"]["valid"].copy()
        task = Task.objects.create(
            name=data["name"],
            description=data["description"],
            author=self.user1,
            status=self.status,
            executor=self.user2,
        )
        self.assertEqual(task.name, data["name"])
        self.assertEqual(task.description, data["description"])

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("CreateTask"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("Login"))


class TestUpdateTask(DownloadTasks):
    def test_create_view(self):
        response = self.client.get(reverse_lazy("UpdateTask", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("UpdateTask", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("Login"))


class TestDeleteTask(DownloadTasks):
    def test_create_view(self):
        response = self.client.get(reverse_lazy("DeleteTask", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("DeleteTask", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("Login"))

    def test_delete_user_no_author(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy("DeleteTask", kwargs={"pk": 2}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("TasksList"))
