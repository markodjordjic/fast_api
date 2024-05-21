import unittest
from fastapi.testclient import TestClient
from app.body_updates import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUp(self) -> None:
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
            'name': 'Foo', 
            'description': None, 
            'price': 50.2, 
            'tax': 10.5, 
            'tags': []
        }

        response = self.app.put("/items/baz", json=specification)

        actual = response.json()
    
        self.assertDictEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_read_items'))
    suite.addTest(TestExercise('test_update_items'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())