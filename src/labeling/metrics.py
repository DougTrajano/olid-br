import pandas as pd
from typing import Any, List, Union

def percent_agreement(reliability_data: Union[List[List[Any]], pd.DataFrame] = None) -> float:
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
    
    agree_on = 0
    non_agree_on = 0
    for annotations in zip(*reliability_data):
        if len(set(annotations)) == 1:
            agree_on += 1
        else:
            non_agree_on += 1
    return agree_on / (agree_on + non_agree_on)