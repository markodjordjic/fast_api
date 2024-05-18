import unittest
from fastapi.testclient import TestClient
from app.handling_errors import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_read_item(self) -> None:

        expected = {'item': 'The Foo Wrestlers'}
        
        response = self.app.get("/items/foo")

        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_read_item_custom_error(self) -> None:

        expected = {'detail': 'Item not found.'}
        
        response = self.app.get("/items/fooooo")

        actual = response.json()
    
        self.assertEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_read_item'))
    suite.addTest(TestExercise('test_read_item_custom_error'))
    
    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())