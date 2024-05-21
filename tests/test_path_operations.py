import unittest
from fastapi.testclient import TestClient
from app.path_operations import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_create_item(self) -> None:

        expected = 201

        payload = {
            'name': 'Chips',
            'description': 'Salted potato chips',
            'price': 9.,
            'tax': 11.,
            'tags': []
        }

        response = self.app.post("/items/", json=payload)

        actual = response.status_code
    
        self.assertEqual(actual, expected)

    def test_create_item_wh_tag(self) -> None:

        expected = {
            'name': 'Chips',
            'description': 'Salted potato chips',
            'price': 9.,
            'tax': 11.,
            'tags': []
        }

        specification = {
            'name': 'Chips',
            'description': 'Salted potato chips',
            'price': 9.,
            'tax': 11.
        }

        response = self.app.post("/items_wh_tag/", json=specification)

        actual = response.json()
    
        self.assertEqual(actual, expected)



def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_create_item'))
    suite.addTest(TestExercise('test_create_item_wh_tag'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())