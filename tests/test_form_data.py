import unittest
from fastapi import status
from fastapi.testclient import TestClient
from app.form_data import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_login(self) -> None:

        expected = {'username': 'some_username'}

        specification = {
            "username": "some_username",
            "password": "some_password"
        }

        response = self.app.post("/login/", data=specification)

        actual = response.json()
    
        self.assertEqual(actual, expected)

def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_login'))

    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())