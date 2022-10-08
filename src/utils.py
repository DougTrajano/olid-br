import json
import yaml
import logging
import datetime
import pandas as pd
from .data_classes import RawText
from typing import Dict, Any, List, Union

_logger = logging.getLogger(__name__)


def read_yaml(path: str) -> Dict[Any, Any]:
    """Read a YAML file.
    
    Args:
    - path: The path of the YAML file.

    Returns:
    - A dictionary.
    """
    _logger.debug(f"Reading YAML file: {path}")

    with open(path) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    _logger.debug("YAML file loaded.")
    return data


def read_json(path: str) -> Dict[Any, Any]:
    """Read a JSON file.

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
    """Save data to a JSON file.

    Args:
    - data: The data to save.
    - path: The path of the JSON file.
    """
    _logger.debug(f"Saving data to JSON file: {path}")

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    _logger.debug("Data saved.")

def label_studio_fmt(data: RawText) -> Dict[Any, Any]:
    """Format data to the Label Studio format.
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
                "toxicity_score": data.toxicity_score,
                "category": data.publisher_category
            }
        }
    }

    _logger.debug(f"Formatted data: {fmt_data}")

    return fmt_data

def get_toxic_substrings(text: str, spans: List[int], verbose=False) -> List[str]:
    """Extract string words based on a list of spans.

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
    """Normalize RawText to a list of dictionaries.

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

def check_words(text: str, words: list):
    """Check if the text only contains words from the list.

    Args:
    - text: The text to check.
    - words: The words to check for.

    Returns:
    - True if the text contains all the words.
    """
    for word in words:
        if word not in text:
            return False
    return True
    
def prepare_data_to_px(df: pd.DataFrame):
    """Prepare the data to be used in a plotly graph.

    Args:
    - data: A pandas dataframe with each column being an annotator and each row being a label.

    Returns:
    - A pandas dataframe with the following columns: Annotator, Label, Count.
    """
    data = []

    for annotator in df.columns:
        for label, count in df[annotator].value_counts().items():
            data.append({"Annotator": annotator, "Label": label, "Count": count})
    return pd.DataFrame(data)

def dict_serialize_date(data: List[Dict[Any, Any]], keys: List[Any]):
    """Serialize keys that are dates in a list of dictionaries to ISO 8601.

    Args:
    - data: A list of RawText objects.
    - keys: A list of keys to serialize.

    Returns:
    - A list of dictionaries.
    """
    new_data = []
    for i in data:
        for key in keys:
            if key in i:
                if isinstance(i[key], datetime.datetime):
                    i[key] = i[key].isoformat()
        new_data.append(i)
    return new_data

def get_lead_time(data: Dict[str, Any]):
    """Returns the lead time of the given data (Label Studio JSON format).

    Args:
    - data: A dictionary containing the data.

    Returns:
    - A list of floats representing the lead time.
    """
    lead_times = []

    for item in data:
        for annotation in item["annotations"]:
            if "lead_time" in annotation.keys():
                lead_times.append(annotation["lead_time"])
    return lead_times

def get_annotations_by_rater(ratings: Dict[str, pd.DataFrame], rater: int, item: int):
    """Get all annotations by rater.

    Args:
    - ratings: Dictionary of ratings. e.g. {"health": health, "ideology": ideology, ...}
    - rater: Rater ID
    - item: Item ID

    Returns:
    - List of annotations by rater (e.g ["insult", "profanity_obscene", ...])
    """
    annotations = []
    for k, v in ratings.items():
        if rater in v.columns:
            if v[rater].loc[item] == True:
                annotations.append(k)
    return annotations
    