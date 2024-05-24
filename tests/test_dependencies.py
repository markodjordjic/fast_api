import unittest
from copy import deepcopy
from fastapi.testclient import TestClient
from app.dependecies.dependencies import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_read_items(self) -> None:

        expected = {
            'q': 'test query',
            'skip': 5,
            'limit': 20
        }

        parameters = {
            'q': 'test query',
            'skip': 5,
            'limit': 20
        }

        response = self.app.get("/items/", params=parameters)

        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_read_items_wh_commons(self) -> None:

        expected = {
            'q': 'test query',
            'items': [
                {'item_name': 'Foo'},
                {'item_name': 'Bar'}
            ]
        }

        parameters = {
            'q': 'test query',
            'skip': 0,
            'limit': 2
        }

        response = self.app.get("/items_wh_commons/", params=parameters)

        actual = response.json()
    
        self.assertEqual(actual, expected)



def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_read_items'))
    suite.addTest(TestExercise('test_read_items_wh_commons'))
 
    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())