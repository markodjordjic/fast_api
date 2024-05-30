import unittest
from fastapi.testclient import TestClient
from app.security.base import app as base_app
from app.security.get_current_user import app as user_app
from app.security.get_user_and_pw import app as user_pw_app
from app.security.get_user_and_pw_jwt import app as user_pw_jwt_app

class TestBaseApp(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=base_app)

    def test_read_items(self) -> None:

        expected = {'detail': 'Not authenticated'}

        response = self.app.get("items/")

        actual = response.json()
    
        self.assertEqual(actual, expected)

class TestUserApp(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=user_app)

    def test_read_users_me(self) -> None:

        expected = {'detail': 'Not authenticated'}

        response = self.app.get("users/me")

        actual = response.json()
    
        self.assertEqual(actual, expected)

class TestUserPWApp(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=user_pw_app)

    def test_login(self) -> None:

        expected = {'access_token': 'johndoe', 'token_type': 'bearer'}

        payload = {
            "username": "johndoe",
            "password": "secret"            
        }

        response = self.app.post("/token/", data=payload)

        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_login_wrong_pw(self) -> None:

        expected = '{"detail":"Incorrect password"}'

        payload = {
            "username": "johndoe",
            "password": "wrong_password"            
        }

        response = self.app.post("/token/", data=payload)

        actual = response.text
    
        self.assertEqual(actual, expected)

    def test_login_wrong_un(self) -> None:

        expected = '{"detail":"Incorrect username"}'

        payload = {
            "username": "john",
            "password": "secret"            
        }

        response = self.app.post("/token/", data=payload)

        actual = response.text
    
        self.assertEqual(actual, expected)

class TestUserPWJWTApp(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    def setUp(self) -> None:
        self.app = TestClient(app=user_pw_jwt_app)

    def _authorize(self) -> str:

        payload = {
            "username": "johndoe",
            "password": "secret"            
        }

        authorization = self.app.post("/token", data=payload)
        token_type = authorization.json()['token_type']
        access_token = authorization.json()['access_token']
        token_type_and_token = f"{token_type} {access_token}"

        return token_type_and_token


    def test_login_for_access_token(self) -> None:

        expected = 200

        payload = {
            "username": "johndoe",
            "password": "secret"            
        }

        response = self.app.post("/token", data=payload)

        actual = response.status_code
    
        self.assertEqual(actual, expected)

    def test_read_users_me(self) -> None:

        expected = [{'item_id': 'Foo', 'owner': 'johndoe'}]

        token_type_and_token = self._authorize()
        
        response = self.app.get(
            url='/users/me/items', 
            headers={
                'accept': 'application/json',
                'Authorization': token_type_and_token 
            }
        )            

        actual = response.json()
    
        self.assertEqual(actual, expected)

    def test_read_own_items(self) -> None:

        expected = {
            'username': 'johndoe', 
            'email': 'johndoe@example.com',
            'full_name': 'John Doe',
            'disabled': False
        }

        token_type_and_token = self._authorize()

        response = self.app.get(
            url='/users/me/', 
            headers={
                'accept': 'application/json',
                'Authorization': token_type_and_token 
            }
        )            

        actual = response.json()
    
        self.assertEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestBaseApp('test_read_items'))
    suite.addTest(TestUserApp('test_read_users_me'))
    suite.addTest(TestUserPWApp('test_login'))
    suite.addTest(TestUserPWApp('test_login_wrong_pw'))
    suite.addTest(TestUserPWApp('test_login_wrong_un'))
    suite.addTest(TestUserPWApp('test_login_wrong_un'))
    suite.addTest(TestUserPWJWTApp('test_login_for_access_token'))
    suite.addTest(TestUserPWJWTApp('test_read_users_me'))
    suite.addTest(TestUserPWJWTApp('test_read_own_items'))

    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())