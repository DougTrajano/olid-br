import os
import shutil
import numpy as np
from typing import List, Dict, Any


def prep_data(X: List[str], Y: List[int], classes: Dict[Any, int] = None):
    """Prepare data (X, Y) in a list.

    Args:
    - X: list of strings (texts)
    - Y: List of ints (0 or 1)
    - classes: dictionary of classess ({class_id: class_name, ...})

    Returns:
    - data: list of tuples (X, y)
    """
    def get_key_by_value(dictionary: Dict[Any, Any], value: Any):
        "Get key by value in dictionary"
        return next(key for key, val in dictionary.items() if val == value)

    data = []
    for x, y in zip(X, Y):
        if classes is not None:
            y = get_key_by_value(classes, y)
        data.append([x, y])
    return data

def clean_simpletransformers(folders: List[str] = ["cache_dir", "outputs", "runs"]):
    """Clean simpletransformers folders.

    Args:
    - folders: list of folders to clean
    """
    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder, ignore_errors=True)

def compute_pos_weight(y: np.ndarray) -> List[float]:
    """Compute positive weight for class imbalance.

    Args:
    - y: array-like of shape (n_samples, n_classes)
    Returns:
    - pos_weight: array-like of shape (n_classes,)
    """
    pos_weight = []
    for i in range(len(y[0])):
        positives = y[:, i].sum()
        negatives = len(y[:, i]) - positives
        pos_weight.append(negatives / positives)
    return pos_weight

def get_labels_for_y(y: List[int], toxicity_labels: List[int]):
    """
    Get the toxicity labels from the y.
    Args:
    - y: List of labels.
    - toxicity_labels: List of toxicity labels.
    Returns:
    - List of toxicity labels.
    """
    labels = []
    for i in range(len(y)):
        if y[i] == 1:
            labels.append(toxicity_labels[i])
    return labels