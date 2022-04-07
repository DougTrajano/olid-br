import json
import pytest
import datetime
from typing import Dict, List, Any
from src.data_models import RawText, ProcessedText
from src.utils import (
    read_yaml,
    save_json,
    read_json,
    label_studio_fmt,
    get_toxic_substrings,
    normalize_raw_text
)

now = datetime.datetime.now()

TESTS = [
    (RawText(id=1,
          text="Text sequence",
          source="Twitter",
          created_at=now,
          collected_at=now,
          is_toxic=False,
          toxicity_score=0.01),
     {
        "data": {
            "text": "Text sequence",
            "ref_id": 1,
            "meta_info": {
                    "source": "Twitter",
                    "created_at": now.isoformat(),
                    "collected_at": now.isoformat(),
                    "is_toxic": False,
                    "toxicity_score": 0.01
            }
        }
    })
]

TESTS_SUBSTRINGS = [
    (ProcessedText(
        id="6391e3dbb12848ac8ef6131edf2d69f9",
        text="USER Canalha URL",
        is_offensive="OFF",
        is_targeted="TIN",
        targeted_type="IND",
        toxic_spans=[5, 6, 7, 8, 9, 10, 11, 12],
        health=False,
        ideology=False,
        insult=True,
        lgbtqphobia=False,
        other_lifestyle=False,
        physical_aspects=False,
        profanity_obscene=False,
        racism=False,
        religious_intolerance=False,
        sexism=False,
        xenophobia=False
    ), 
    ["Canalha "]
    )
]

def test_read_yam():
    assert type(read_yaml('properties/application.yaml')) == dict
    print(f"TEST OK for src.utils.read_yaml")

def test_read_json():
    # Open properties/application.yaml and save as JSON
    data = read_yaml("properties/application.yaml")
    with open("properties/application.json", "w") as outfile:
        json.dump(data, outfile)
    assert type(read_json('properties/application.json')) == dict
    print(f"TEST OK for src.utils.read_json")

def test_save_json():
    # Open properties/application.yaml and save as JSON
    data = read_yaml("properties/application.yaml")
    save_json(data, "properties/application.json")
    assert type(read_json('properties/application.json')) == dict
    print(f"TEST OK for src.utils.save_json")

@pytest.mark.parametrize("value, output", TESTS)
def test_label_studio_fmt(value: RawText, output: Dict[str, Dict[str, Any]]):
    assert label_studio_fmt(value) == output
    print(f"TEST OK for src.metadata.label_studio_fmt() - Value: {value} - Output: {output}")

@pytest.mark.parametrize("value, output", TESTS_SUBSTRINGS)
def test_get_toxic_substrings(value: ProcessedText, output: List[str]):
    assert get_toxic_substrings(value.text, value.toxic_spans) == output
    print(f"TEST OK for src.metadata.get_toxic_substrings() - Value: {value} - Output: {output}")
