import pytest
import logging
from src.logs import setup_logger

TESTS = [
    ("DEBUG"),
    ("INFO"),
    ("WARNING"),
    ("ERROR"),
    ("CRITICAL")
]

@pytest.mark.parametrize("loglevel", TESTS)
def test_logger(loglevel: str):
    _logger = setup_logger(loglevel)
    assert type(_logger) == logging.Logger