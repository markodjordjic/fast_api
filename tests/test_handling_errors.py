import unittest
from fastapi.testclient import TestClient
from app.handling_errors import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUpClass(self) -> None:
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

    def test_read_item_header(self) -> None:

        expected = 'Some error message.'
        
        response = self.app.get("/items-header/food")

        actual = response.headers['x-error']

        self.assertEqual(actual, expected)


    def test_read_unicorn(self) -> None:

        expected = '{"message":"Oops! yolo did something. There goes a rainbow..."}'
        
        response = self.app.get("/unicorns/yolo")

        actual = response.text

        self.assertEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_read_item'))
    suite.addTest(TestExercise('test_read_item_custom_error'))
    suite.addTest(TestExercise('test_read_item_header'))
    suite.addTest(TestExercise('test_read_unicorn'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())