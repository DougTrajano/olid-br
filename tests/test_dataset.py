import pytest
import pathlib
from src.dataset import Dataset
from src.utils import read_yaml
from src.data_classes import (
    Annotator,
    LabelStrategy
)


TESTS = [
    {
        "raw": {
            "id": "string",
            "data": {
                "text": "string",
                "meta_info": {
                    "source": "string",
                    "created_at": "string",
                    "collected_at": "string",
                    "toxicity_score": 0.5
                }
            },
            "label_assignment": LabelStrategy()
        }
    }
]

# @pytest.mark.parametrize("raw, label_assignment", [(i["raw"], i["label_assignment"]) for i in TESTS])
# def test_dataset(raw, label_assignment):
#     """Test the dataset class."""

#     # Load annotators
#     annotators = read_yaml(
#         pathlib.Path(__file__).parent.parent / "properties" / "annotators.yaml"
#     )

#     annotators = [Annotator(**annotator) for annotator in annotators]

#     dataset = Dataset(annotators)
#     assert dataset.build(raw, label_assignment) == dict
