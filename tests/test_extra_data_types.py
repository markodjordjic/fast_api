from datetime import datetime, time, timedelta
from uuid import UUID
from pydantic import BaseModel
from fastapi.testclient import TestClient
import unittest
from app.extra_data_types import app


class TestExercise(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
 
    @classmethod
    def setUp(self) -> None:
        self.app = TestClient(app=app)

    def test_read_items(self) -> None:

        expected = {
            'item_id': '00000000-0000-0000-0000-000000000080', 
            'start_datetime': '2024-06-01T12:00:00', 
            'end_datetime': '2024-06-01T12:10:00', 
            'process_after': 864000.0, 
            'repeat_at': None, 
            'start_process': '2024-06-11T12:00:00', 
            'duration': -863400.0
        }

        class Item(BaseModel):
            start_datetime: datetime
            end_datetime: datetime
            process_after: timedelta
            repeat_at: time | None

        item_specification = {
            'start_datetime': datetime(
                year=2024, 
                month=6, 
                day=1, 
                hour=12, 
                minute=0, 
                second=0
            ),
            'end_datetime': datetime(
                year=2024, 
                month=6, 
                day=1, 
                hour=12, 
                minute=10, 
                second=0
            ),
            'process_after': timedelta(seconds=10*24*60*60),
            'repeat_at': None
        }

        item = Item(**item_specification)

        url = "/items/" + str(UUID(int=128))

        response = self.app.put(
            url=url,
            content=item.model_dump_json()
        )

        actual = response.json()
    
        self.assertDictEqual(actual, expected)

    @classmethod
    def tearDownClass(self) -> None:
        self.app = None

def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestExercise('test_read_items'))
    
    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(test_suite())