import os
import json
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from typing import List, Dict

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