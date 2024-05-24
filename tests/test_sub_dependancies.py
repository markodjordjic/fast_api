import unittest
from copy import deepcopy
from fastapi.testclient import TestClient
from app.dependecies.sub_dependencies import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_read_query_wh_query(self) -> None:

        expected = {
            'q_or_cookie': 'test query'
        }

        parameters = {
            'q': 'test query'
        }

        response = self.app.get("/items/", params=parameters)

        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_read_query_wo_query(self) -> None:

        expected = {
            'q_or_cookie': None
        }

        response = self.app.get("/items/")

        actual = response.json()
    
        self.assertEqual(actual, expected)



def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_read_query_wh_query'))
    suite.addTest(TestExercise('test_read_query_wo_query'))
 
    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())