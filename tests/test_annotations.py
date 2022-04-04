import pytest
from src.annotations import (
    has_32_annotator,
    get_is_offensive,
    get_offensive_type,
    get_targeted_type,
    get_is_targeted,
    get_toxic_spans
)

def test_has_32_annotator():
    annotations = [
        {
            "completed_by": 32,
            "result": [
                {
                    "from_name": "is_toxic",
                    "value": {
                        "choices": [
                            "Yes"
                        ]
                    }
                }
            ]
        }
    ]
    assert has_32_annotator(annotations)
    print(f"TEST OK for src.annotations.has_32_annotator()")

def test_get_is_offensive():
    annotations = [
        {
            "completed_by": 32,
            "result": [
                {
                    "from_name": "is_toxic",
                    "value": {
                        "choices": [
                            "Yes"
                        ]
                    }
                }
            ]
        },
        {
            "completed_by": 1,
            "result": [
                {
                    "from_name": "is_toxic",
                    "value": {
                        "choices": [
                            "No"
                        ]
                    }
                }
            ]
        },
        {
            "completed_by": 32,
            "result": [
                {
                    "from_name": "is_toxic",
                    "value": {
                        "choices": [
                            "No"
                        ]
                    }
                }
            ]
        },
        {
            "completed_by": 1,
            "result": [
                {
                    "from_name": "is_toxic",
                    "value": {
                        "choices": [
                            "Yes"
                        ]
                    }
                }
            ]
        },    
    ]
    assert get_is_offensive([annotations[0]]) == "OFF"
    assert get_is_offensive([annotations[1]]) == "NOT"
    assert get_is_offensive([annotations[2]]) == "NOT"
    assert get_is_offensive([annotations[3]]) == "OFF"
    print(f"TEST OK for src.annotations.get_is_offensive()")

def test_get_offensive_type():
    annotations = [
        {
            "completed_by": 32,
            "result": [
                {
                    "type": "choices",
                    "value": {
                        "choices": [
                            "Insult"
                        ]
                    },
                    "origin": "manual",
                    "to_name": "text",
                    "from_name": "Sentiment"
                }
            ]
        },
        {
            "completed_by": 1,
            "result": [
                {
                    "type": "choices",
                    "value": {
                        "choices": [
                            "Insult"
                        ]
                    },
                    "origin": "manual",
                    "to_name": "text",
                    "from_name": "Sentiment"
                }
            ]
        },
        {
            "completed_by": 32,
            "result": [
                {
                    "type": "choices",
                    "value": {
                        "choices": [
                            "Insult"
                        ]
                    },
                    "origin": "manual",
                    "to_name": "text",
                    "from_name": "Sentiment"
                }
            ]
        },
        {
            "completed_by": 1,
            "result": [
                {
                    "type": "choices",
                    "value": {
                        "choices": [
                            "Insult"
                        ]
                    },
                    "origin": "manual",
                    "to_name": "text",
                    "from_name": "Sentiment"
                }
            ]
        }
    ]
    assert get_offensive_type([annotations[0]], "Insult") == True
    assert get_offensive_type([annotations[1]], "Insult") == True
    assert get_offensive_type([annotations[2]], "Health") == False
    assert get_offensive_type([annotations[3]], "Health") == False
    print(f"TEST OK for src.annotations.get_offensive_type()")


def test_get_targeted_type():
    annotations = [
        {
            "completed_by": 32,
            "result": [
                {
                    "from_name": "target",
                    "value": {
                        "choices": [
                            "Individual"
                        ]
                    }
                }
            ]
        },
        {
            "completed_by": 32,
            "result": [
                {
                    "from_name": "target",
                    "value": {
                        "choices": [
                            "Group"
                        ]
                    }
                }
            ]
        },
        {
            "completed_by": 32,
            "result": [
                {
                    "from_name": "target",
                    "value": {
                        "choices": [
                            "Other"
                        ]
                    }
                }
            ]
        },
        {
            "completed_by": 1,
            "result": [
                {
                    "from_name": "target",
                    "value": {
                        "choices": [
                            "Individual"
                        ]
                    }
                }
            ]
        },
        {
            "completed_by": 1,
            "result": [
                {
                    "from_name": "target",
                    "value": {
                        "choices": [
                            "Group"
                        ]
                    }
                }
            ]
        },
        {
            "completed_by": 1,
            "result": [
                {
                    "from_name": "target",
                    "value": {
                        "choices": [
                            "Other"
                        ]
                    }
                }
            ]
        }
    ]
    assert get_targeted_type([annotations[0]]) == "IND"
    assert get_targeted_type([annotations[1]]) == "GRP"
    assert get_targeted_type([annotations[2]]) == "OTH"
    assert get_targeted_type([annotations[3]]) == "IND"
    assert get_targeted_type([annotations[4]]) == "GRP"
    assert get_targeted_type([annotations[5]]) == "OTH"
    print(f"TEST OK for src.annotations.get_targeted_type()")

def test_get_is_targeted():
    annotations = [
        {
            "completed_by": 32,
            "result": [
                {
                    "from_name": "is_toxic",
                    "value": {
                        "choices": [
                            "Yes"
                        ]
                    }
                }
            ]
        },
        {
            "completed_by": 32,
            "result": [
                {
                    "from_name": "target",
                    "value": {
                        "choices": [
                            "Individual"
                        ]
                    }
                }
            ]
        },
        {
            "completed_by": 32,
            "result": [
                {
                    "from_name": "target",
                    "value": {
                        "choices": [
                            "Group"
                        ]
                    }
                }
            ]
        },
        {
            "completed_by": 32,
            "result": [
                {
                    "from_name": "target",
                    "value": {
                        "choices": [
                            "Other"
                        ]
                    }
                }
            ]
        },
    ]
    assert get_is_targeted([annotations[0]]) == "UNT"
    assert get_is_targeted([annotations[1]]) == "TIN"
    assert get_is_targeted([annotations[2]]) == "TIN"
    assert get_is_targeted([annotations[3]]) == "TIN"
    print(f"TEST OK for src.annotations.get_is_targeted()")

def test_get_toxic_spans():
    annotations = [
        {
            "completed_by": 32,
            "result": [
                {
                    "from_name": "BadWords",
                    "value": {
                        "end": 13,
                        "text": "Canalha ",
                        "start": 5,
                        "labels": [
                            "Curse words"
                        ]
                    }
                }
            ]
        }
    ]
    assert get_toxic_spans(annotations) == [5, 6, 7, 8, 9, 10, 11, 12]
    print(f"TEST OK for src.annotations.get_toxic_spans()")
