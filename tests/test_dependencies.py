import unittest
from copy import deepcopy
from fastapi.testclient import TestClient
from app.dependencies.dependencies import app as dependency_app
from app.dependencies.sub_dependencies import app as sub_dependency_app


class TestDependencies(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=dependency_app)

    def test_read_items(self) -> None:

        expected = {
            'q': 'test query',
            'skip': 5,
            'limit': 20
        }

        parameters = {
            'q': 'test query',
            'skip': 5,
            'limit': 20
        }

        response = self.app.get("/items/", params=parameters)

        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_read_items_wh_commons(self) -> None:

        expected = {
            'q': 'test query',
            'items': [
                {'item_name': 'Foo'},
                {'item_name': 'Bar'}
            ]
        }

        parameters = {
            'q': 'test query',
            'skip': 0,
            'limit': 2
        }

        response = self.app.get("/items_wh_commons/", params=parameters)

        actual = response.json()
    
        self.assertEqual(actual, expected)


class TestSubDependencies(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=sub_dependency_app)

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
    suite.addTest(TestDependencies('test_read_items'))
    suite.addTest(TestDependencies('test_read_items_wh_commons'))
    suite.addTest(TestSubDependencies('test_read_query_wh_query'))
    suite.addTest(TestSubDependencies('test_read_query_wo_query'))

 
    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())