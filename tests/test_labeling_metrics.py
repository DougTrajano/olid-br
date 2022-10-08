import pytest
import numpy as np
from src.labeling.metrics import (
    percent_agreement,
    disagreement_by_raters,
    disagreement_score
)

RELIABILITY_DATA = np.array(
    [[1, 1, 0, 0, 0, 1],  # CoderA
     [1, 1, 1, 0, 1, 0],  # CoderB
     [1, 1, 0, 0, 1, 0]]  # CoderC
).T.tolist()


@pytest.mark.parametrize("reliability_data, expected", [(RELIABILITY_DATA, 0.5)])
def test_percent_agreement(reliability_data, expected):
    """Test the percent agreement function."""
    print(percent_agreement(reliability_data))
    assert percent_agreement(reliability_data) == expected


@pytest.mark.parametrize("reliability_data, label, expected", [(RELIABILITY_DATA, 1, {1: 2, 2: 1, 3: 2})])
def test_disagreement_by_raters(reliability_data, label, expected):
    """Test the disagreement by raters function."""
    print(disagreement_by_raters(reliability_data, label))
    assert disagreement_by_raters(reliability_data, label) == expected


@pytest.mark.parametrize("reliability_data, label, expected", [(RELIABILITY_DATA, 1, 0.6)])
def test_disagreement_score(reliability_data, label, expected):
    """Test the disagreement score function."""
    print(disagreement_score(reliability_data, label))
    assert disagreement_score(reliability_data, label) == expected
