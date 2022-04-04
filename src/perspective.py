import time
import logging
from retrying import retry
from typing import Dict
from googleapiclient import discovery

_logger = logging.getLogger()


class PerspectiveAPI(object):
    def __init__(self, apikey: str, wait_time: float = 0.1):
        """
        Initialize the Perspective API client.

        Parameters:
            apikey (str): The API key to use for the API.
            wait_time (float): The time to wait between requests in seconds.
        """
        self.wait_time = wait_time
        discovery_service_url = "https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1"

        self.client = discovery.build("commentanalyzer",
                                      "v1alpha1",
                                      developerKey=apikey,
                                      discoveryServiceUrl=discovery_service_url,
                                      static_discovery=False)

        _logger.debug(f"Created PerspectiveAPI object.")

    @retry(stop_max_attempt_number=3, wait_random_min=1000, wait_random_max=1500)
    def predict(self, text: str) -> Dict[str, float]:
        """
        Predict toxicity of a comment.

        Parameters:
            text (str): The text to predict toxicity for.

        Returns:
            A dictionary containing the predicted toxicity scores. (e.g. {'TOXICITY': 0.5})
        """
        _logger.debug(f"Predicting for text: {text}")

        analyze_request = {
            "comment": {"text": text},
            "languages": ["pt"],
            "requestedAttributes": {"TOXICITY": {}}
        }

        response = self.client.comments().analyze(body=analyze_request).execute()

        _logger.debug(f"Got response: {response}")
        
        try:
            toxicity = response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
            toxicity = round(toxicity, 4)
        except Exception as error:
            _logger.error(f"Error getting toxicity: {error}")
            toxicity = None
        
        time.sleep(self.wait_time)
        
        _logger.debug(f"Finished predicting for text: {text}")
        return {"TOXICITY": toxicity}