import json
import pytest
import datetime
from typing import Dict, Any
from src.data_models import RawText
from src.utils import read_yaml, read_json, label_studio_fmt

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



@pytest.mark.parametrize("value, output", TESTS)
def test_label_studio_fmt(value: RawText, output: Dict[str, Dict[str, Any]]):
    assert label_studio_fmt(value) == output
    print(f"TEST OK for src.metadata.label_studio_fmt() - Value: {value} - Output: {output}")
