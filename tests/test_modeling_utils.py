import pathlib
import numpy as np
from dotenv import load_dotenv

load_dotenv(pathlib.Path(__file__).parent.parent / ".env")

from src.modeling.utils import (
    prep_data,
    clean_simpletransformers,
    compute_pos_weight
)

def test_prep_data():
    """Test the prep_data function."""
    X = ["text1", "text2"]
    Y = [0, 1]
    data = prep_data(X, Y)
    assert data == [["text1", 0], ["text2", 1]]

def test_clean_simpletransformers():
    """Test the clean_simpletransformers function."""
    clean_simpletransformers()
    assert True

def test_compute_pos_weight():
    """Test the compute_pos_weight function."""
    y = np.array([[0, 1], [1, 0]])
    pos_weight = compute_pos_weight(y)
    assert pos_weight == [1.0, 1.0]
