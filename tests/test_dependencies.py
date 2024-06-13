import unittest
from copy import deepcopy
from fastapi.testclient import TestClient
from app.dependencies.dependencies import app as dependency_app
from app.dependencies.sub_dependencies import app as sub_dependency_app
from app.dependencies.path_operation_decorators import app as \
    path_operation_app
from app.dependencies.global_dependencies import app as \
    global_dependencies_app
from app.dependencies.yield_dependencies import app as \
    yield_dependencies_app
from app.dependencies.yield_dependencies_internal import app as \
    yield_dependencies_internal_app
from app.dependencies.yield_dependencies_internal import InternalError

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

        expected = {'q_or_cookie': 'test query'}

        parameters = {'q': 'test query'}

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

class TestPathOperationDecorators(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=path_operation_app)

    def test_read_items(self) -> None:

        expected = [{'item': 'Foo'}, {'item': 'Bar'}]

        headers = {
            'x-token': 'fake-super-secret-token',
            'x-key': 'fake-super-secret-key'
        }

        response = self.app.get("/items/", headers=headers)

        actual = response.json()
    
        self.assertListEqual(actual, expected)

    def test_read_items_wrong_header(self) -> None:

        expected = 400

        headers = {'x-token': 'some-token', 'x-key': 'some-key'}

        response = self.app.get("/items/", headers=headers)

        actual = response.status_code
    
        self.assertEqual(actual, expected)


class TestGlobalDependencies(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=global_dependencies_app)

    def test_read_items(self) -> None:

        expected = [{'item': 'Portal Gun'}, {'item': 'Plumbus'}]

        headers = {
            'x-token': 'fake-super-secret-token',
            'x-key': 'fake-super-secret-key'
        }

        response = self.app.get("/items/", headers=headers)

        actual = response.json()
    
        self.assertListEqual(actual, expected)

    def test_read_items_wrong_header(self) -> None:

        expected = 400

        headers = {
            'x-token': 'some-token',
            'x-key': 'some-key'
        }

        response = self.app.get("/items/", headers=headers)

        actual = response.status_code
    
        self.assertEqual(actual, expected)


class TestYieldDependencies(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=yield_dependencies_app)

    def test_read_items(self) -> None:

        expected = {"description": "Gun to create portals", "owner": "Rick"}

        response = self.app.get("/items/portal-gun")

        actual = response.json()
    
        self.assertDictEqual(actual, expected)

    def test_read_items_owner_error(self) -> None:

        expected = b'{"detail":"Owner error: Rick"}'

        response = self.app.get("/items/plumbus")

        actual = response.content
    
        self.assertEqual(actual, expected)

    def test_read_items_error(self) -> None:

        expected = 404

        response = self.app.get("/items/some-item")

        actual = response.status_code
    
        self.assertEqual(actual, expected)


class TestYieldDependenciesInternal(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=yield_dependencies_internal_app)

    def test_get_items(self) -> None:

        expected = 'The portal gun is too dangerous to be owned by Rick'
  
        with self.assertRaises(InternalError) as context:
            self.app.get("/items/portal-gun")
        actual = context.exception.args[0]     

        self.assertEqual(expected, actual)

    def test_get_items_correct(self) -> None:

        expected = b'"plumbus"'
  
        response = self.app.get("/items/plumbus")

        actual = response.content 

        self.assertEqual(expected, actual)

    def test_get_items_not_correct(self) -> None:

        expected = 404
  
        response = self.app.get("/items/plum")

        actual = response.status_code 

        self.assertEqual(expected, actual)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestDependencies('test_read_items'))
    suite.addTest(TestDependencies('test_read_items_wh_commons'))
    suite.addTest(TestSubDependencies('test_read_query_wh_query'))
    suite.addTest(TestSubDependencies('test_read_query_wo_query'))
    suite.addTest(TestPathOperationDecorators('test_read_items'))
    suite.addTest(TestPathOperationDecorators('test_read_items_wrong_header'))
    suite.addTest(TestGlobalDependencies('test_read_items'))
    suite.addTest(TestGlobalDependencies('test_read_items_wrong_header'))
    suite.addTest(TestYieldDependencies('test_read_items'))
    suite.addTest(TestYieldDependencies('test_read_items_owner_error'))
    suite.addTest(TestYieldDependencies('test_read_items_error'))
    suite.addTest(TestYieldDependenciesInternal('test_get_items'))
    suite.addTest(TestYieldDependenciesInternal('test_get_items_correct'))
    suite.addTest(TestYieldDependenciesInternal('test_get_items_not_correct'))

    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())