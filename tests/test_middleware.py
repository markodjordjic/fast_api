import unittest
from fastapi.testclient import TestClient
from app.middleware import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_http(self) -> None:

        expected = 0.0

        response = self.app.get("/")

        actual = float(response.headers.get('x-process-time'))
    
        self.assertAlmostEqual(actual, expected)

def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_http'))

    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())