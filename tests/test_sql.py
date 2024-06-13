import unittest
from fastapi.testclient import TestClient
from app.db import app
from app.sql.schemas import UserCreate


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUpClass(self) -> None:
        self.app = TestClient(app=app)

    def test_create_user(self) -> None:

        user_specification = {
            'email': 'alexander.mccane@google.com',
            'password': 'May122@@4'
        }

        user_create = UserCreate(
            **user_specification
        )

        response = self.app.post("/users/", json=user_create.model_dump())

        expected = {
            'email': 'alexander.mccane@google.com', 
            'id': 1, 
            'is_active': True, 
            'items': []
        }
        actual = response.json()
    
        self.assertEqual(actual, expected)

    @classmethod
    def tearDownClass(cls) -> None:
        
        return super().tearDownClass()

def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_create_user'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())