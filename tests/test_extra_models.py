import unittest
from pydantic import EmailStr
from fastapi.testclient import TestClient
from app.extra_models import app, UserIn


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_create_user(self) -> None:

        expected = {
            "username": "Peter McLaughlin",
            "email": "peter.mclaughlin@skydive.com", 
            "full_name": None
        }

        user_in = UserIn(**{
            'username': 'Peter McLaughlin',
            'password': 'wee',
            'email': 'peter.mclaughlin@skydive.com'            
        })
        
        response = self.app.post("/user/", json=user_in.model_dump())

        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_read_item_union(self) -> None:
       
        expected = {
            'description': 'All my friends drive a low rider', 
            'type': 'car'
        }

        response = self.app.get("/items_union/item1")

        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_read_kw_weights(self) -> None:

        expected = {"foo": 2.3, "bar": 3.4}

        response = self.app.get("/keyword-weights")

        actual = response.json()
    
        self.assertEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_create_user'))
    suite.addTest(TestExercise('test_read_item_union'))
    suite.addTest(TestExercise('test_read_kw_weights'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())