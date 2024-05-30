import unittest
from fastapi.testclient import TestClient
from app.cors import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    @unittest.skip
    def test_root(self) -> None:
        """Test is just a placeholder

        The objective to test different origins is not satisfied. 
        Further experimentation is needed.

        """

        response = self.app.get(
            "/", 
            headers={
                'accept': 'application/json',
                'Origin': 'bla'
            }
        )

        actual = response.json()
    
        self.assertEqual(actual, actual)

def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_root'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())