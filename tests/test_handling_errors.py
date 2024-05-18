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

        expected = {}
        
        response = self.app.get('items/{800}')

        actual = response.json()
    
        self.assertEqual(actual, expected)

def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_read_item'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())