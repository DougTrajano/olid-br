from src.labeling.assignment import (
    majority_vote,
    at_least_one,
    all_true,
    all_labeled_spans
)

ANNOTATIONS = [
    [True, True, True],
    [True, True, False],
    [True, False, False],
    [False, False, False]
]

ANNOTATIONS_SPANS = [
    [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
    [[0, 1, 2], [0, 1, 2], [0, 1]],
    [[0, 1, 2], [0, 1], [0, 1]],
    [[0, 1], [0, 1], [0, 1]]
]

def test_majority_vote():
    """Test the majority_vote function."""
    assert majority_vote(ANNOTATIONS[0]) == True
    assert majority_vote(ANNOTATIONS[1]) == True
    assert majority_vote(ANNOTATIONS[2]) == False
    assert majority_vote(ANNOTATIONS[3]) == False

def test_at_least_one():
    """Test the at_least_one function."""
    assert at_least_one(ANNOTATIONS[0]) == True
    assert at_least_one(ANNOTATIONS[1]) == True
    assert at_least_one(ANNOTATIONS[2]) == True
    assert at_least_one(ANNOTATIONS[3]) == False

def test_all_true():
    """Test the all_true function."""
    assert all_true(ANNOTATIONS[0]) == True
    assert all_true(ANNOTATIONS[1]) == False
    assert all_true(ANNOTATIONS[2]) == False
    assert all_true(ANNOTATIONS[3]) == False

def test_all_labeled_spans():
    """Test the all_labeled_spans function."""
    assert all_labeled_spans(ANNOTATIONS_SPANS[0]) == [0, 1, 2]
    assert all_labeled_spans(ANNOTATIONS_SPANS[1]) == [0, 1, 2]
    assert all_labeled_spans(ANNOTATIONS_SPANS[2]) == [0, 1, 2]
    assert all_labeled_spans(ANNOTATIONS_SPANS[3]) == [0, 1]
