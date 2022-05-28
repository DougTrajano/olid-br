import numpy as np
import pandas as pd
from typing import Any, Dict, List, Union


def percent_agreement(reliability_data: Union[List[List[Any]], pd.DataFrame]) -> float:
    """Calculate the percentage agreement between raters.

    Args:
    - reliability_data: The reliability data. Format is as follows:
            [[1, 1, 0, ..., 0, 0, 1], # CoderA
             [1, 1, 1, ..., 0, 1, 0], # CoderB
             [1, 1, 0, ..., 0, 1, 0]] # CoderC
            each row is a list of annotations by a given annotator

    Returns:
    - The percentage agreement as a float.
    """
    if isinstance(reliability_data, pd.DataFrame):
        reliability_data = reliability_data.transpose().values.tolist()
    elif isinstance(reliability_data, list):
        reliability_data = np.array(reliability_data).T.tolist()
    else:
        raise ValueError("reliability_data must be a list or a DataFrame.")

    agree_on = 0
    non_agree_on = 0
    for annotations in zip(*reliability_data):
        if len(set(annotations)) == 1:
            agree_on += 1
        else:
            non_agree_on += 1
    return agree_on / (agree_on + non_agree_on)


def disagreement_by_raters(reliability_data: Union[List[List[Any]], pd.DataFrame],
                           label: Any) -> Dict[int, int]:
    """Calculate the disagreement between raters.

    Args:
    - reliability_data: The reliability data. Format is as follows:
            [[1, 1, 0, ..., 0, 0, 1], # CoderA
             [1, 1, 1, ..., 0, 1, 0], # CoderB
             [1, 1, 0, ..., 0, 1, 0]] # CoderC
            each row is a list of annotations by a given annotator
    - label: The label to be used to calculate the disagreement rates.

    Returns:
    - A list of disagreement rates for number of raters.
    """
    if isinstance(reliability_data, pd.DataFrame):
        reliability_data = reliability_data.transpose().values.tolist()
    elif isinstance(reliability_data, list):
        reliability_data = np.array(reliability_data).T.tolist()
    else:
        raise ValueError("reliability_data must be a list or a DataFrame.")

    n_coders = len(reliability_data)

    disagrements = {i+1: 0 for i in range(n_coders)}

    for annotations in zip(*reliability_data):
        if label in annotations:
            coders_with_label = [
                i for i, a in enumerate(annotations) if a == label]
            disagrements[len(coders_with_label)] += 1

    return disagrements


def disagreement_score(reliability_data: Union[List[List[Any]], pd.DataFrame],
                       label: Any) -> float:
    """Calculate the disagreement rate.

    Args:
    - reliability_data: The reliability data. Format is as follows:
            [[1, 1, 0, ..., 0, 0, 1], # CoderA
             [1, 1, 1, ..., 0, 1, 0], # CoderB
             [1, 1, 0, ..., 0, 1, 0]] # CoderC
            each row is a list of annotations by a given annotator
    - label: The label to be used to calculate the disagreement rates.

    Returns:
    - The disagreement rate as a float.
    """
    dis = disagreement_by_raters(reliability_data, label)
    
    try:
        score = (sum(dis.values())-dis[len(dis)]) / sum(dis.values())
    except ZeroDivisionError:
        score = 0
    return score
