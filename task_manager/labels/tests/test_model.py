from .files import DownloadLabels


class TestLabelModel(DownloadLabels):
    def test_task_model(self):
        self.assertEqual(self.label_1.name, "Label_One")
        self.assertEqual(self.label_3.name, "Label_Three")
        self.assertEqual(self.count, 3)
