import unittest
from fastapi.testclient import TestClient
from app.string_validations import app

client = TestClient(app)

class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)


    def test_read_from_list(self) -> None:
 
        response = client.get("/items_list/?query=Element%201&query=Element%202")
 
        assert response.status_code == 200
        assert response.json()['query'] == ['Element 1', 'Element 2']


    def test_read_from_list_default(self) -> None:
 
        response = client.get("/items_list_default")
 
        assert response.status_code == 200
        assert response.json()['query'] == ['Element 1', 'Element 2']



def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_read_from_list'))
    suite.addTest(TestExercise('test_read_from_list_default'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())