import pytest
import pathlib
import datetime
from src.dataset import Dataset
from src.utils import read_yaml
from src.data_classes import (
    Annotation,
    Annotator,
    LabelStrategy,
    Metadata,
    ProcessedText,
    Text
)


TESTS = [
    (
        {
            "id": 120096,
            "annotations": [
                {
                    "id": 8849,
                    "completed_by": 127,
                    "result": [
                        {
                            "id": "ocn_b9b9ks",
                            "type": "choices",
                            "value": {
                                    "choices": [
                                        "Yes"
                                    ]
                            },
                            "origin": "manual",
                            "to_name": "text",
                            "from_name": "is_toxic"
                        },
                        {
                            "id": "J5lRL5-r5V",
                            "type": "labels",
                            "value": {
                                    "end": 87,
                                    "text": "altou um beijinho gay estilo Jesus ",
                                    "start": 52,
                                    "labels": [
                                        "toxic spans"
                                    ]
                            },
                            "origin": "manual",
                            "to_name": "text",
                            "from_name": "toxic_spans"
                        },
                        {
                            "id": "hoW3242n9i",
                            "type": "choices",
                            "value": {
                                    "choices": [
                                        "Insult"
                                    ]
                            },
                            "origin": "manual",
                            "to_name": "text",
                            "from_name": "toxic_labels"
                        }
                    ],
                    "was_cancelled": False,
                    "ground_truth": False,
                    "created_at": "2022-05-04T18:36:20.774657Z",
                    "updated_at": "2022-05-04T18:36:20.774693Z",
                    "lead_time": 17.069,
                    "prediction": {},
                    "result_count": 0,
                    "task": 126096,
                    "parent_prediction": None,
                    "parent_annotation": None
                },
                {
                    "id": 9916,
                    "completed_by": 126,
                    "result": [
                        {
                            "id": "ANQiwany5x",
                            "type": "choices",
                            "value": {
                                    "choices": [
                                        "Yes"
                                    ]
                            },
                            "origin": "manual",
                            "to_name": "text",
                            "from_name": "is_toxic"
                        },
                        {
                            "id": "uLIrr0ZJsd",
                            "type": "choices",
                            "value": {
                                    "choices": [
                                        "Insult",
                                        "Profanity\/Obscene"
                                    ]
                            },
                            "origin": "manual",
                            "to_name": "text",
                            "from_name": "toxic_labels"
                        },
                        {
                            "id": "6xnY_HmhuN",
                            "type": "choices",
                            "value": {
                                    "choices": [
                                        "Individual"
                                    ]
                            },
                            "origin": "manual",
                            "to_name": "text",
                            "from_name": "target_type"
                        }
                    ],
                    "was_cancelled": False,
                    "ground_truth": False,
                    "created_at": "2022-05-05T20:18:42.435867Z",
                    "updated_at": "2022-05-05T20:18:46.440781Z",
                    "lead_time": 7341.931,
                    "prediction": {},
                    "result_count": 0,
                    "task": 120096,
                    "parent_prediction": None,
                    "parent_annotation": None
                },
                {
                    "id": 4468,
                    "completed_by": 128,
                    "result": [
                        {
                            "id": "vAGtQ33zwv",
                            "type": "choices",
                            "value": {
                                    "choices": [
                                        "Yes"
                                    ]
                            },
                            "origin": "manual",
                            "to_name": "text",
                            "from_name": "is_toxic"
                        },
                        {
                            "id": "UUFcMGoRSF",
                            "type": "choices",
                            "value": {
                                    "choices": [
                                        "Insult",
                                        "Religious Intolerance"
                                    ]
                            },
                            "origin": "manual",
                            "to_name": "text",
                            "from_name": "toxic_labels"
                        }
                    ],
                    "was_cancelled": False,
                    "ground_truth": False,
                    "created_at": "2022-04-27T00:28:16.081817Z",
                    "updated_at": "2022-04-27T00:28:16.081835Z",
                    "lead_time": 4.352,
                    "prediction": {},
                    "result_count": 0,
                    "task": 123096,
                    "parent_prediction": None,
                    "parent_annotation": None
                }
            ],
            "file_upload": "5923f2ec-olid-br-phase-2.json",
            "drafts": [],
            "predictions": [],
            "data": {
                "text": "USER Adorei o comercial também Jesus. Só achei que faltou um beijinho gay estilo Jesus e USER sabe?! Rsrsrs",
                "ref_id": "Ugi0SZvwXIV_rHgCoAEC.8-fB3HYAUKo7-L1_uPYzKW",
                "meta_info": {
                        "source": "YouTube",
                        "is_toxic": True,
                        "created_at": "2015-05-29T09:27:57",
                        "collected_at": "2022-04-08T08:03:44.134767",
                        "toxicity_score": 0.7189
                }
            },
            "meta": {},
            "created_at": "2022-04-13T03:51:02.479346Z",
            "updated_at": "2022-05-05T20:18:46.374365Z",
            "project": 14
        },
        LabelStrategy(),
        ["processed_texts", "metadata", "full_texts"]
    )
]


@ pytest.mark.parametrize("item, label_assignment, expected", TESTS)
def test_dataset(item, label_assignment, expected):
    """Test the dataset class."""

    # Load annotators
    annotators = read_yaml(
        pathlib.Path(__file__).parent.parent / "properties" / "annotators.yaml"
    )

    annotators = [Annotator(**annotator) for annotator in annotators]

    dataset = Dataset(annotators)
    assert list(dataset.build([item], label_assignment).keys()) == expected
