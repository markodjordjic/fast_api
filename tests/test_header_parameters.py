import unittest
from fastapi.testclient import TestClient
from app.header_parameters import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUpClass(self) -> None:
        self.app = TestClient(app=app)

    def test_read_items(self) -> None:

        header = {'user_agent': 'user agent'}

        response = self.app.get("/items/", headers=header)

        expected = {
            'User-Agent': 'testclient'
        }
        actual = response.json()
    
        self.assertEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_read_items'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())