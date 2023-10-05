from django.urls import reverse_lazy
from .files import DownloadTasks
from task_manager.tasks.models import Task


class TestTasksList(DownloadTasks):
    def test_tasks_view(self):
        response = self.client.get(reverse_lazy("tasks"))
        self.assertEqual(response.status_code, 200)

    def test_tasks_content(self):
        response = self.client.get(reverse_lazy("tasks"))
        self.assertQuerySetEqual(
            response.context["object_list"], self.tasks, ordered=False
        )

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("tasks"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))


class TestFilterTask(DownloadTasks):
    def teat_task_filter_by_label(self):
        response = self.client.get(
            reverse_lazy("tasks"), {"labels": self.label1.pk}
        )
        self.assertEqual(response.context["tasks"].count(), 2)
        self.assertContains(response, self.task_1.name)
        self.assertContains(response, self.task_3.name)

    def test_task_filter_by_status(self):
        response = self.client.get(
            reverse_lazy("tasks"), {"status": self.status1.pk}
        )
        self.assertEqual(response.context["object_list"].count(), 1)
        self.assertContains(response, self.task_2.name)

    def test_task_by_executor(self):
        response = self.client.get(
            reverse_lazy("tasks"), {"executor": self.user2.pk}
        )
        self.assertEqual(response.context["object_list"].count(), 2)
        self.assertContains(response, self.task_1.name)
        self.assertContains(response, self.task_2.name)

    def test_task_filter_by_own_task(self):
        response = self.client.get(
            reverse_lazy("tasks"), {"author_task": self.user1.pk}
        )
        self.assertEqual(response.context["object_list"].count(), 1)


class TestTaskView(DownloadTasks):
    def test_task_view(self):
        response = self.client.get(reverse_lazy("task_show", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task_1.name)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("task_show", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_task_content(self):
        response = self.client.get(reverse_lazy("task_show", kwargs={"pk": 1}))
        self.assertEqual(response.context["task"].name, self.task_1.name)
        self.assertEqual(response.context["task"].author, self.task_1.author)


class TestCreateTask(DownloadTasks):
    def test_create_view(self):
        response = self.client.get(reverse_lazy("task_create"))
        self.assertEqual(response.status_code, 200)

    def test_task_create(self):
        data = self.new_task["create"]["valid"].copy()
        task = Task.objects.create(
            name=data["name"],
            description=data["description"],
            author=self.user1,
            status=self.status1,
            executor=self.user2,
        )
        self.assertEqual(task.name, data["name"])
        self.assertEqual(task.description, data["description"])

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(reverse_lazy("task_create"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))


class TestUpdateTask(DownloadTasks):
    def test_create_view(self):
        response = self.client.get(
            reverse_lazy("task_update", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 200)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(
            reverse_lazy("task_update", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))


class TestDeleteTask(DownloadTasks):
    def test_create_view(self):
        response = self.client.get(
            reverse_lazy("task_delete", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 200)

    def test_user_no_login_view(self):
        self.client.logout()
        response = self.client.get(
            reverse_lazy("task_delete", kwargs={"pk": 1})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_delete_user_no_author(self):
        self.client.force_login(self.user1)
        response = self.client.get(
            reverse_lazy("task_delete", kwargs={"pk": 2})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("tasks"))
