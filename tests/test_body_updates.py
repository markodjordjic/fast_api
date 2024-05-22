import unittest
from copy import deepcopy
from fastapi.testclient import TestClient
import app.body_updates as bu
from app.body_updates import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.original_items = deepcopy(bu.items)  # Protect original data.
        self.app = TestClient(app=app)

    def test_read_items(self) -> None:

        expected = {
            'name': 'Foo', 
            'description': None, 
            'price': 50.2, 
            'tax': 10.5, 
            'tags': []
        }

        response = self.app.get("/items/foo")

        actual = response.json()
    
        self.assertDictEqual(actual, expected)

    def test_update_items(self) -> None:

        specification = {
            'name': 'Chips',
            'description': 'Potato chips, salted', 
            'price': 9., 
            'tax': 3.2, 
            'tags': ['Indulgence', 'Snack']
        }

        expected = {
            'name': 'Chips',
            'description': 'Potato chips, salted', 
            'price': 9., 
            'tax': 3.2, 
            'tags': ['Indulgence', 'Snack']        
        }

        response = self.app.put("/update_items/baz", json=specification)

        actual = response.json()
    
        self.assertDictEqual(actual, expected)

    def test_partial_update_items(self) -> None:

        specification = {
            'name': 'Chips',
            'description': 'Potato chips, salted', 
            'tags': ['Indulgence', 'Snack']
        }

        expected = {
            'name': 'Chips',
            'description': 'Potato chips, salted', 
            'price': 50.2, 
            'tax': 10.5, 
            'tags': ['Indulgence', 'Snack']        
        }

        response = self.app.patch("/items/baz", json=specification)

        actual = response.json()
    
        self.assertDictEqual(actual, expected)

    def tearDown(self) -> None:

        bu.items = self.original_items  # Resetting the data after every test.

def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_read_items'))
    suite.addTest(TestExercise('test_update_items'))
    suite.addTest(TestExercise('test_partial_update_items'))
    
    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())