import pytest
import datetime
from src.metadata import get_time_shift

TESTS = [
    (datetime.datetime(2021, 1, 1, 10, 0, 0), "morning"),
    (datetime.datetime(2021, 2, 14, 6, 0, 0), "morning"),
    (datetime.datetime(2021, 6, 21, 14, 0, 0), "afternoon"),
    (datetime.datetime(2021, 4, 1, 18, 0, 0), "evening"),
    (datetime.datetime(2021, 3, 5, 20, 0, 0), "evening"),
    (datetime.datetime(2021, 8, 10, 23, 0, 0), "night"),
    (datetime.datetime(2021, 9, 25, 5, 0, 0), "night")
]


@pytest.mark.parametrize("value, output", TESTS)
def test_get_time_shift(value: datetime.datetime, output: str):
    assert get_time_shift(value) == output
    print(f"TEST OK for src.metadata.get_time_shift() - Input: {value} - Output: {output}")
