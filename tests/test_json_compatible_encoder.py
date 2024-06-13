import unittest
from fastapi.testclient import TestClient
from app.json_compatible_encoder import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUpClass(self) -> None:
        self.app = TestClient(app=app)

    def test_update_item(self) -> None:

        expected = {
            'test': {
                'title': 'Seinfeld Chronicles',
                'timestamp': '2024-05-21T00:00:00',
                'description': 'The Show about Nothing'
            }
        }

        specification = {
            'title': 'Seinfeld Chronicles',
            'timestamp': '2024-05-21 00:00:00',
            'description': 'The Show about Nothing'
        }

        response = self.app.put("/items/test", json=specification)

        actual = response.json()
    
        self.assertDictEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_update_item'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())