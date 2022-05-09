
import warnings
from collections import Counter
from typing import Any, List

def majority_vote(annotations: List[Any]):
    """Returns the majority vote of the annotations.

    Args:
    - annotations: A list of annotations.

    Returns:
    - The majority vote of the annotations.
    """
    # Raise an warning if the annotation list is even
    if len(annotations) % 2 == 0:
        warnings.warn("The annotation list is even. The returned vote will be random.")

    return max(Counter(annotations).items(), key=lambda x: x[1])[0]

def at_least_one(annotations: List[bool]):
    """Returns True if at least one of the annotations is True.

    Args:
    - annotations: A list of annotations.

    Returns:
    - True if at least one of the annotations is True.
    """
    return any(annotations)

def all_labeled_spans(annotations: List[Any]):
    """Returns all spans that are labeled by at least one annotator.

    Args:
    - annotations: A list of annotations.

    Returns:
    - A list of spans (e.g. [0, 1, 2, ...]).
    """
    spans = []
    for annotation in annotations:
        spans.extend(annotation)
    spans = list(set(spans))
    spans.sort()
    return spans