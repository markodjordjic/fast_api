import unittest
from fastapi.testclient import TestClient
from app.response_model import app, Item


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_create_item(self) -> None:

        specification = { 
            "name": "Chips",
            "description": "Potato chips, salted",
            "price": 99.0,
            "tax": 11.0,
        }

        item = Item(**specification)

        response = self.app.post("/items/", content=item.model_dump_json())

        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_read_items(self) -> None:

        pass


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_create_item'))
    suite.addTest(TestExercise('test_read_items'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())