import re
import logging
import spacy

_logger = logging.getLogger()

class Anonymizer(object):
    def __init__(self, user_placeholder: str = "USER", url_placeholder: str = "URL",
                 hashtag_placeholder: str = "HASHTAG", spacy_model: str = "pt_core_news_lg"):
        self.user_placeholder = user_placeholder
        self.url_placeholder = url_placeholder
        self.hashtag_placeholder = hashtag_placeholder

        self.nlp = spacy.load(spacy_model)
        self.nlp.add_pipe("emoji", first=True)

        _logger.debug("Anonymizer initialized")

    def apply_all(self, text: str) -> str:
        """Applies all anonymization methods to a given text.

        Args:
        - The text to be anonymized.

        Returns:
        - The anonymized text.
        """
        _logger.debug(f"Anonymizing text: {text}")

        text = self.remove_users(text)
        text = self.remove_urls(text)
        text = self.remove_hashtags(text)
        text = self.remove_names(text)

        _logger.debug(f"Anonymized text: {text}")
        
        return text

    def remove_users(self, text: str) -> str:
        """Regex that removes user mentions on a given text.

        Args:
        - The text to be anonymized.

        Returns:
        - The anonymized text.
        """
        return re.sub(r'@\w+', self.user_placeholder, text)
        
    def remove_urls(self, text: str) -> str:
        """Regex that removes urls on a given text.

        Args:
        - The text to be anonymized.

        Returns:
        - The anonymized text.
        """
        return re.sub(r'http\S+', self.url_placeholder, text)

    def remove_hashtags(self, text: str) -> str:
        """Regex that removes hashtags on a given text.

        Args:
        - The text to be anonymized.

        Returns:
        - The anonymized text.
        """
        return re.sub(r'#\S+', self.hashtag_placeholder, text)

    def remove_names(self, text: str):
        """Removes names from a given text.

        Arguments:
        - text: The text to be anonymized.

        Returns:
        - The anonymized text.
        """
        doc = self.nlp(text)

        for token in doc:
            if token.pos_ == "PROPN" and token._.emoji_desc is None and token.dep_ in ["ROOT", "nsubj", "flat:name", "conj"]:
                text = text.replace(token.text, self.user_placeholder)
        return text