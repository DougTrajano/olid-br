import os
import json
import shutil
import numpy as np
import pandas as pd
from typing import List, Dict, Any
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(
        output_files: str | List[str] = "train.csv") -> Dict[str, Dict | pd.DataFrame]:
    """Download dataset from Kaggle.

    Args:
    - output_files: List of files to be outputted.

    Returns:
    - A dictionary with the output files as keys and the content as values.
    """
    files = [
        "olidbr.csv.zip",
        "train.csv",
        "test.csv",
        "train_metadata.csv",
        "test_metadata.csv",
        "train.json",
        "test.json",
        "additional_data.json"
    ]

    # Download OLID-BR dataset
    for file in files:
        if not os.path.exists(file):
            print(f"Downloading OLID-BR from Kaggle.")
            kaggle = KaggleApi()
            kaggle.authenticate()
            kaggle.dataset_download_files(dataset="olidbr", unzip=True)

    # Load data
    result = {}
    
    output_files = output_files if isinstance(output_files, list) else [output_files]

    for file in output_files:
        if file.endswith(".csv"):
            result[file] = pd.read_csv(file)
        elif file.endswith(".json"):
            result[file] = json.load(open(file, "r"))
        else:
            raise ValueError(f"File {file} is not supported.")

    # Delete files
    for file in files:
        if os.path.exists(file):
            os.remove(file)

    return result

def get_dataset_version() -> int:
    """Get dataset version

    Returns:
    - Dataset version: int
    """
    kaggle = KaggleApi()
    olidbr = kaggle.dataset_view(dataset="olidbr")
    return olidbr.currentVersionNumber

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
    