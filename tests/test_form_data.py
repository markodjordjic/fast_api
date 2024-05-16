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

    def test_update_items(self) -> None:

        expected = status.HTTP_201_CREATED

        response = self.app.post("/items/?name=test")

        actual = response.status_code
    
        self.assertEqual(actual, expected)

    def test_get_or_create_existing_task(self) -> None:

        expected = status.HTTP_200_OK

        response = self.app.put("get-or-create-task/foo")

        actual = response.status_code
    
        self.assertEqual(actual, expected)

    def test_get_or_create_new_task(self) -> None:

        expected = status.HTTP_201_CREATED

        response = self.app.put("get-or-create-task/fighters")

        actual = response.status_code
    
        self.assertEqual(actual, expected)

def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_update_items'))
    suite.addTest(TestExercise('test_get_or_create_existing_task'))
    suite.addTest(TestExercise('test_get_or_create_new_task'))

    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())