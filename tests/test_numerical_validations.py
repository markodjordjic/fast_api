import unittest
from fastapi.testclient import TestClient
from app.numerical_validations import app

client = TestClient(app=app)

class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)


    def test_read_items(self) -> None:

        response = client.get("/read_items/800/?item-query=M")

        expected = {'item_id': 800, 'q': 'M'}
        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_read_items_ge(self) -> None:

        response = client.get("/read_items_ge/20/?q=M")

        expected = 'Input should be greater than or equal to 50'
        actual = response.json()['detail'][0]['msg']
    
        self.assertEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_read_items'))
    suite.addTest(TestExercise('test_read_items_ge'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())