import unittest
from fastapi.testclient import TestClient
from app.background_tasks import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_send_notification(self) -> None:

        expected = {'message': 'Message sent'}
    
        response = self.app.post("/send-notification/email.adress%40email.com")

        actual = response.json()
    
        self.assertDictEqual(actual, expected)



def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_send_notification'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())