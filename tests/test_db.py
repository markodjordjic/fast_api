import unittest
unittest.TestLoader.sortTestMethodsUsing = None
from fastapi.testclient import TestClient
from app.db import app

class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def _create_user(self):
        """Needed for test_update

        """
        payload = {
            'email': 'test.user@someweb.com',
            'password': 'this_is_a_trivial_password',
            'id': 800,
            'is_active': True
        }
           
        self.app.post("/users/", json=payload)


    @classmethod
    def setUpClass(self) -> None:
        self.app = TestClient(app=app)

    def test_create_user(self) -> None:
        """Will be utilized for testing of reading

        """

        payload = {
            'email': 'alexander.mccane@google.com',
            'password': 'May122@@4'
        }
           
        response = self.app.post("/users/", json=payload)

        expected = {
            'email': 'alexander.mccane@google.com', 
            'id': 1, 
            'is_active': True, 
            'items': []
        }

        actual = response.json()
    
        self.assertDictEqual(actual, expected)

    def test_read_user(self) -> None:
        
        response = self.app.get("/user/1")

        expected = {
            'email': 'alexander.mccane@google.com', 
            'id': 1, 
            'is_active': True, 
            'items': []
        }

        actual = response.json()

        self.assertDictEqual(actual, expected)
    
    def test_update_user(self) -> None:

        expected = {
            'title': 'Chips', 
            'description': 
            'Salted potato chips', 
            'id': 1, 
            'owner_id': 1
        }

        items = {
            'title': 'Chips', 
            'description': 'Salted potato chips'
        }
        
        response = self.app.post("/users/1/item/", json=items)

        actual = response.json()

        self.assertDictEqual(actual, expected)


    def test_delete_user(self) -> None:

        payload = {
            'email': 'alexander.mccane@google.com',
            'password': 'May122@@4'
        }
   
        response = self.app.post("/delete_user/", json=payload)

        expected = 'User alexander.mccane@google.com deleted.'

        actual = response.json()
    
        self.assertEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_create_user'))
    suite.addTest(TestExercise('test_read_user'))
    suite.addTest(TestExercise('test_update_user'))
    suite.addTest(TestExercise('test_delete_user'))
    
    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())