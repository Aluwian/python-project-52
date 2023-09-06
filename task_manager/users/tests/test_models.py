from .files import DownloadUsers


class MyTestCase(DownloadUsers):
    def test_user_model(self):
        self.assertEqual(self.user_1.username, "Anna_K")
        self.assertEqual(self.user_2.first_name, "Gerasim")
        self.assertEqual(self.count, 3)
