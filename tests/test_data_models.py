import pytest
import datetime
from typing import Dict, Any
from src.data_classes import (
    Annotator,
    RawText,
    ProcessedText,
    Metadata
)

ANNOTATORS = [
    {
        "id": "123456789",
        "annotator_id": 1,
        "gender": "Male",
        "age": 31,
        "education_level": "high school",
        "annotator_type": "volunteer",
        "background": "Social Science",
    },
    {
        "id": "987654321",
        "annotator_id": 2,
        "gender": "Female",
        "age": 29,
        "education_level": "bachelor's degree",
        "annotator_type": "researcher",
        "background": "Computer Science"
    }
]

RAW_TESTS = [
    {
        "id": 1,
        "text": "This is a normal text",
        "source": "Twitter",
        "created_at": datetime.datetime.now(),
        "is_toxic": False,
        "toxicity_score": 0.32
    },
    {
        "id": 2,
        "text": "This is a offensive text",
        "source": "Twitter",
        "created_at": datetime.datetime.now(),
        "is_toxic": True,
        "toxicity_score": 0.67,
        "publisher_category": "news"
    }
]

PROCESSED_TESTS = [
    {
        "id": "123456789",
        "text": "This is a normal text",
        "is_offensive": "NOT",
        "is_targeted": "UNT",
        "toxic_spans": None,
        "health": False,
        "lgbtqphobia": False,
        "ideology": False,
        "insult": False,
        "other_lifestyle": False,
        "physical_aspects": False,
        "profanity_obscene": False,
        "racism": False,
        "religious_intolerance": False,
        "sexism": False,
        "xenophobia": False
    },
    {
        "id": "987654321",
        "text": "This is a offensive text fuck",
        "is_offensive": "OFF",
        "is_targeted": "TIN",
        "toxic_spans": [25, 26, 27, 28, 29],
        "health": False,
        "lgbtqphobia": False,
        "ideology": False,
        "insult": True,
        "other_lifestyle": False,
        "physical_aspects": False,
        "profanity_obscene": False,
        "racism": False,
        "religious_intolerance": False,
        "sexism": False,
        "xenophobia": False
    }
]

METADATA = [
    {
        "id": "123456789",
        "source": "Twitter",
        "created_at": datetime.datetime.now(),
        "collected_at": datetime.datetime.now(),
        "toxicity_score": 0.32,
    },
    {
        "id": "987654321",
        "source": "Facebook",
        "created_at": datetime.datetime.now(),
        "collected_at": datetime.datetime.now(),
        "toxicity_score": 0.67,
        "category": "news"
    }

]

@pytest.mark.parametrize("data", ANNOTATORS)
def test_annotator(data: Dict[str, Any]):
    test = Annotator(**data)
    assert type(test.dict()) == dict
    print(f"TEST OK for src.data_models.Annotator - Input: {data}")

@pytest.mark.parametrize("data", RAW_TESTS)
def test_raw_text(data: Dict[str, Any]):
    test = RawText(**data)
    assert type(test.dict()) == dict
    print(f"TEST OK for src.data_models.RawText - Input: {data}")

@pytest.mark.parametrize("data", PROCESSED_TESTS)
def test_processed_text(data: Dict[str, Any]):
    test = ProcessedText(**data)
    assert type(test.dict()) == dict
    print(f"TEST OK for src.data_models.ProcessedText - Input: {data}")

@pytest.mark.parametrize("data", METADATA)
def test_metadata(data: Dict[str, Any]):
    test = Metadata(**data)
    assert type(test.dict()) == dict
    print(f"TEST OK for src.data_models.Metadata - Input: {data}")
