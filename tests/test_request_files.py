import csv
import io
import sys
import unittest
from fastapi import UploadFile
from fastapi.testclient import TestClient
from app.request_files import app
import tempfile

def create_file():

    content = [
        ['This', 'is', 'a', 'simple', 'text', 'file.'],
        ['It', 'has', 'two', 'sentences.']
    ]

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(content)

    return output.getvalue()

class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUp(self) -> None:
        self.app = TestClient(app=app)
        self.test_data = create_file()

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_create_file(self) -> None:

        expected = {'file_size': 87}

        response = self.app.post("/files/", data={"file":self.test_data})

        actual = response.json()

    
        self.assertEqual(actual, expected)

    @unittest.expectedFailure
    def test_create_upload_file(self) -> None:
        #TODO: Make the test pass.

        expected = {'filename': 'test_file'}

        with tempfile.SpooledTemporaryFile(mode='wb') as fp:
            fp.write(b'Hello world!')
            fp.seek(0)

        upload_file = UploadFile(file=fp)
        upload_file.filename = 'test_file'

        response = self.app.post("/upload_file/", data={"file": upload_file})

        actual = response.json()
    
        self.assertEqual(actual, expected)


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_create_file'))
    suite.addTest(TestExercise('test_create_upload_file'))

    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())