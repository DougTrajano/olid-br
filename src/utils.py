import os
import json
import yaml
import boto3
import logging
from src.data_models import RawText
from typing import Dict, Any, List, Union

_logger = logging.getLogger(__name__)


def read_yaml(path: str) -> Dict[Any, Any]:
    "Read a YAML file."
    _logger.debug(f"Reading YAML file: {path}")

    with open(path) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    _logger.debug("YAML file loaded.")
    return data


def read_json(path: str) -> Dict[Any, Any]:
    """
    Read a JSON file.

    Args:
    - path: The path of the JSON file.

    Return:
    - The data of the JSON file.
    """
    _logger.debug(f"Reading JSON file: {path}")

    with open(path, encoding="utf-8") as file:
        data = json.load(file)
        
    _logger.debug("JSON file loaded.")
    return data

def save_json(data: Union[Dict, List[Dict]], path: str) -> None:
    """
    Save data to a JSON file.

    Args:
    - data: The data to save.
    - path: The path of the JSON file.
    """
    _logger.debug(f"Saving data to JSON file: {path}")

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    _logger.debug("Data saved.")

def label_studio_fmt(data: RawText) -> Dict[Any, Any]:
    """
    Format data to the Label Studio format.
    https://labelstud.io/guide/tasks.html#Basic-Label-Studio-JSON-format

    "created_at" and "collected_at" will be converted to ISO 8601.

    Arguments:
        data (Text): Data record.

    Return:
        Data formated to Label Studio.
    """
    _logger.debug(f"Formatting data: {data.dict()}")

    fmt_data = {
        "data": {
            "text": data.text,
            "ref_id": data.id,
            "meta_info": {
                "source": data.source,
                "created_at": data.created_at.isoformat(),
                "collected_at": data.collected_at.isoformat(),
                "is_toxic": data.is_toxic,
                "toxicity_score": data.toxicity_score
            }
        }
    }

    _logger.debug(f"Formatted data: {fmt_data}")

    return fmt_data

def get_toxic_substrings(text: str, spans: List[int], verbose=False) -> List[str]:
    """
    Extract string words based on a list of spans.

    Args:
    - text: The text to extract words from.
    - spans: A list of spans to extract words from.

    Returns:
    - A list of words extracted from the text.
    """
    def format_substring(substring: List[str]) -> str:
        return " ".join("".join(substring).split())

    delimiter = None
    words = []
    tmp = []
    for i in range(len(text)):
        if i in spans:
            if verbose:
                print(f"Found span at {i} ({text[i]})")
            if delimiter is None:
                delimiter = i
            else:
                delimiter += 1
            tmp.append(text[i])
        else:
            tmp.append(" ")

        if delimiter is not None and i != delimiter:
            words.append(format_substring(tmp))
            tmp = []
            delimiter = None

    if len(tmp) > 0:
        words.append(format_substring(tmp))
        
    words = [w for w in words if w not in [" ", ""]]
    return words

def normalize_raw_text(data: List[RawText]) -> List[Dict[Any, Any]]:
    """
    Normalize RawText to a list of dictionaries.

    Args:
    - data: A list of RawText objects.

    Returns:
    - A list of dictionaries.
    """
    new_data = []
    for i in data:
        i = i.dict()
        i["created_at"] = i["created_at"].isoformat()
        i["collected_at"] = i["collected_at"].isoformat()
        new_data.append(i)
    return new_data
