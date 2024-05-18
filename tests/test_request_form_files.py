import unittest
from fastapi.testclient import TestClient
from fastapi import UploadFile
from app.request_forms_files import app
import tempfile

class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    @unittest.expectedFailure
    def test_create_file(self) -> None:

        expected = {}

        with tempfile.SpooledTemporaryFile(mode='wb') as file:
            file.write(b'Hello World')
            file.seek(0)

        data = {
            "file": "file",
            "fileb": (UploadFile(file=file, filename='file.txt')),
            "token": "token"
        }

        response = self.app.post("/files/", data=data)

        actual = response.json()
    
        self.assertEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_create_file'))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())