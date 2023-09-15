from .files import DownloadTasks


class TestTaskModel(DownloadTasks):
    def test_task_model(self):
        self.assertEqual(self.task_1.name, "Task_One")
        self.assertEqual(self.count, 3)
