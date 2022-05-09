import logging
import numpy as np
import krippendorff
from typing import Any, Dict, List
from statsmodels.stats.inter_rater import aggregate_raters, fleiss_kappa

_logger = logging.getLogger(__name__)


class InterRaterReliability(object):
    """Calculate the reliability of the annotations."""
    def __init__(self, reliability_data: List[List[Any]]):
        """Initialize the InterRaterReliability object.
        
        Args:
        - reliability_data: The reliability data. Format is as follows:
                [[1, 1, 0, ..., 0, 0, 1], # CoderA
                 [1, 1, 1, ..., 0, 1, 0], # CoderB
                 [1, 1, 0, ..., 0, 1, 0]] # CoderC
                each row is a list of annotations by a given annotator
        """
        self.reliability_data = reliability_data

    def agreement_score(self, reliability_data: List[List[Any]] = None) -> float:
        """Calculate the agreement score.

        Args:
        - reliability_data: The reliability data. Format is as follows:
                [[1, 1, 0, ..., 0, 0, 1], # CoderA
                 [1, 1, 1, ..., 0, 1, 0], # CoderB
                 [1, 1, 0, ..., 0, 1, 0]] # CoderC
                each row is a list of annotations by a given annotator

        Returns:
        - The agreement score.
        """
        if reliability_data is None:
            reliability_data = self.reliability_data

        agree_on = 0
        non_agree_on = 0
        for annotations in zip(*reliability_data):
            if len(set(annotations)) == 1:
                agree_on += 1
            else:
                non_agree_on += 1
        return agree_on / (agree_on + non_agree_on)

    def krippendorff_alpha(self, reliability_data: List[List[Any]] = None) -> float:
        """Calculate the Krippendorff's alpha.

        Args:
        - reliability_data: The reliability data. Format is as follows:
                [[1, 1, 0, ..., 0, 0, 1], # CoderA
                 [1, 1, 1, ..., 0, 1, 0], # CoderB
                 [1, 1, 0, ..., 0, 1, 0]] # CoderC
                each row is a list of annotations by a given annotator

        Returns:
        - The Krippendorff's alpha.
        """
        if reliability_data is None:
            reliability_data = self.reliability_data

        try:
            score = krippendorff.alpha(
                reliability_data=reliability_data,
                level_of_measurement="nominal")
        except Exception as e:
            _logger.error(f"Error calculating Krippendorff's alpha: {e}")
            score = np.nan
        return score

    def fleiss_kappa(self, reliability_data: List[List[Any]] = None, method="fleiss") -> float:
        """Calculate the Fleiss's Kappa or Randolph's Kappa.

        Args:
        - reliability_data: The reliability data. Format is as follows:
                [[1, 1, 0, ..., 0, 0, 1], # CoderA
                 [1, 1, 1, ..., 0, 1, 0], # CoderB
                 [1, 1, 0, ..., 0, 1, 0]] # CoderC
                each row is a list of annotations by a given annotator

        Returns:
        - The Fleiss's Kappa or Randolph's Kappa.
        """
        if reliability_data is None:
            reliability_data = self.reliability_data

        agg, _ = aggregate_raters(np.array(reliability_data).transpose())
        return fleiss_kappa(agg, method=method)

    def get_all(self, reliability_data: List[List[Any]] = None) -> Dict[str, float]:
        """Get all metrics for the reliability data.

        Args:
        - reliability_data: The reliability data. Format is as follows:
                [[1, 1, 0, ..., 0, 0, 1], # CoderA
                 [1, 1, 1, ..., 0, 1, 0], # CoderB
                 [1, 1, 0, ..., 0, 1, 0]] # CoderC
                each row is a list of annotations by a given annotator
                
        Returns:
        - A dictionary of metrics.
        """
        if reliability_data is None:
            reliability_data = self.reliability_data

        return {
            "percent_agreement": self.agreement_score(reliability_data),
            "krippendorff_alpha": self.krippendorff_alpha(reliability_data),
            "fleiss_kappa": self.fleiss_kappa(reliability_data, method="fleiss"),
            "randolph_kappa": self.fleiss_kappa(reliability_data, method="randolph"),
        }