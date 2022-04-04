import re
import logging

_logger = logging.getLogger()

class Anonymizer(object):
    def __init__(self, user_placeholder: str = "USER", url_placeholder: str = "URL",
                 hashtag_placeholder: str = "HASHTAG"):
        self.user_placeholder = user_placeholder
        self.url_placeholder = url_placeholder
        self.hashtag_placeholder = hashtag_placeholder

        _logger.debug("Anonymizer initialized")

    def apply_all(self, text: str) -> str:
        """
        Applies all anonymization methods to a given text.

        Arguments:
            text (str): The text to be anonymized.

        Returns:
            str: The anonymized text.
        """
        _logger.debug(f"Anonymizing text: {text}")

        text = self.remove_users(text)
        text = self.remove_urls(text)
        text = self.remove_hashtags(text)

        _logger.debug(f"Anonymized text: {text}")
        
        return text

    def remove_users(self, text: str) -> str:
        """
        Regex that removes user mentions on tweets

        Arguments:
            text (str): The text to be anonymized.

        Returns:
            str: The anonymized text.
        """
        return re.sub(r'@\w+', self.user_placeholder, text)
        
    def remove_urls(self, text: str) -> str:
        """
        Regex that removes urls on tweets

        Arguments:
            text (str): The text to be anonymized.

        Returns:
            str: The anonymized text.
        """
        return re.sub(r'http\S+', self.url_placeholder, text)

    def remove_hashtags(self, text: str) -> str:
        """
        Regex that removes hashtags on tweets

        Arguments:
            text (str): The text to be anonymized.

        Returns:
            str: The anonymized text.
        """
        return re.sub(r'#\S+', self.hashtag_placeholder, text)