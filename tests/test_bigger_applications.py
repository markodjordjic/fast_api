import unittest
from fastapi.testclient import TestClient
from app.bigger_applications import app


class TestUsers(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_read_users(self) -> None:

        expected = [{'username': 'Rick'}, {'username': 'Morty'}]

        params = {'token': 'jessica'}

        response = self.app.get("/users", params=params)

        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_read_users_me(self) -> None:

        expected = {"username": "fakecurrentuser"}

        params = {'token': 'jessica'}

        response = self.app.get("/users/me", params=params)

        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_read_user(self) -> None:

        expected = {'username': 'Patrick Armstrong'}

        params = {'token': 'jessica'}

        response = self.app.get("/users/Patrick%20Armstrong", params=params)

        actual = response.json()
    
        self.assertEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestUsers('test_read_users'))
    suite.addTest(TestUsers('test_read_users_me'))
    suite.addTest(TestUsers('test_read_user'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())