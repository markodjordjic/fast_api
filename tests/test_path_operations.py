import unittest
from fastapi.testclient import TestClient
from app.body import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_update_item(self) -> None:

        response = self.app.put("/update_item/800/?q=How%20many%20are%20there?")

        expected = {
            'item_id': 800, 
            'q': 'How many are there?', 
            'item': {
                'name': 'Cake mould', 
                'description': 
                '8" diameter mould from metal.', 
                'base_price': 499.0, 
                'tax': 
                18.0
            }}
        actual = response.json()
    
        self.assertEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_update_item'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())