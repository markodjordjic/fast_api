import unittest
from fastapi.testclient import TestClient
from app.requests import app, Item


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUpClass(self) -> None:
        self.app = TestClient(app=app)

    def test_update_item(self) -> None:

        expected = {
            "item_id": 800,
            "item": { 
                "name": "Chips",
                "description": "Potato chips, salted",
                "price": 99.0,
                "tax": 11.0,
            }
        }

        item_specification = {
            "name": "Chips",
            "description": "Potato chips, salted",
            "price": 99.0,
            "tax": 11.0,
        }

        item = Item(**item_specification)

        response = self.app.put("/items/800", json=item.model_dump())

        actual = response.json()
    
        self.assertDictEqual(actual, expected)

    def test_update_item_wh_field(self) -> None:

        expected = {
            "item_id": 800,
            "item": { 
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

        item_specification = {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
        }

        item = Item(
            **item_specification
        )

        response = self.app.put("/items/800", json=item.model_dump())

        actual = response.json()
    
        self.assertDictEqual(actual, expected)

    def test_update_item_wh_examples(self) -> None:

        expected = {
            "item_id": 800,
            "item": { 
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

        item_specification = {
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        }

        item = Item(
            **item_specification
        )

        response = self.app.put("/items/800", json=item.model_dump())

        actual = response.json()
    
        self.assertDictEqual(actual, expected)



    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_update_item'))
    suite.addTest(TestExercise('test_update_item_wh_field'))
    suite.addTest(TestExercise('test_update_item_wh_examples'))
    
    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())