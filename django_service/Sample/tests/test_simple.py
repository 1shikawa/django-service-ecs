from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('Test is started.')

    @classmethod
    def tearDownClass(cls):
        print('Test is end.')

    def test_comment(self):
        comment = 'テスト'
        self.assertEqual(comment, 'テスト')