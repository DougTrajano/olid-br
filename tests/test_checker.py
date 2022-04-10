import pytest
from typing import Any, Dict
from src.checker import CommentChecker

TEXTS = [
    {"text": " ", "has_alpha": False, "only_contains_anon": True, "has_acceptable_length": True, "is_empty": True},
    {"text": "Short comment", "has_alpha": True, "only_contains_anon": False, "has_acceptable_length": True, "is_empty": False},
    {"text": "USER HASHTAG", "has_alpha": True, "only_contains_anon": True, "has_acceptable_length": True, "is_empty": False},
    {"text": "Long text "*1000, "has_alpha": True, "only_contains_anon": False, "has_acceptable_length": False, "is_empty": False}
]

@pytest.mark.parametrize("case_test", TEXTS)
def test_check_comment(case_test: Dict[str, Any]):
    checker = CommentChecker()
    assert checker.has_alpha(case_test["text"]) == case_test["has_alpha"]
    assert checker.only_contains_anon(case_test["text"]) == case_test["only_contains_anon"]
    assert checker.has_acceptable_length(case_test["text"]) == case_test["has_acceptable_length"]
    assert checker.is_empty(case_test["text"]) == case_test["is_empty"]
    