from typing import List, Union
from langdetect import detect
from google.cloud import translate
from lingua import LanguageDetectorBuilder

class LanguageDetector(object):
    def __init__(self, google_project_id: str = "doug-311118"):
        """Initialize the language detection class.

        Parameters:
        - google_project_id: The Google Cloud project ID.
        """
        self.lingua = LanguageDetectorBuilder.from_all_spoken_languages().build()
        self.google_project_id = google_project_id

    def _lingua(self, text: str):
        """Predict the language of the text using the Lingua Python library.

        Args:
        - text: The text to be predicted.

        Returns:
        - The predicted language.
        """
        pred = self.lingua.detect_language_of(text)
        return pred.__str__().replace("Language.", "")

    def _google(self, text: str):
        """Predict the language of the text using the Google Translate API.
        
        Args:
        - text: The text to be predicted.

        Returns:
        - The predicted language.
        """
        client = translate.TranslationServiceClient()
        parent = f"projects/{self.google_project_id}/locations/global"

        # Detail on supported types can be found here:
        # https://cloud.google.com/translate/docs/supported-formats
        response = client.detect_language(
            content=text,
            parent=parent,
            mime_type="text/plain")

        # Display list of detected languages sorted by detection confidence.
        # The most probable language is first.
        for language in response.languages:
            return {
                "text": text,
                "language_code": language.language_code,
                "confidence": language.confidence
            }
            
    def _predict(self, text: str):
        """Predict the language of the text using all available methods.
            langdetect -> lingua -> Google Translate API

        Args:
        - text: The text to be predicted.

        Returns:
        - The predicted language.
        """
        # Using langdetect
        pred = detect(text)
        if pred == "pt":
            return pred
        else:
            # Using lingua
            pred = self._lingua(text)
            if pred == "PORTUGUESE":
                return "pt"
            else:
                # Using Google Translate API
                return self._google(text)["language_code"]

    def predict(self, data: Union[List[str], str], raise_on_error: bool = True):
        """Predict the language of the text or list of texts using all available methods.
            langdetect -> lingua -> Google Translate API

        Args:
        - data: The text or list of texts to be predicted.

        Returns:
        - The predicted language(s).
        """
        if isinstance(data, str):
            try:
                return self._predict(data)
            except Exception as e:
                if raise_on_error:
                    raise e
                else:
                    return None
        else:
            preds = []
            for text in data:
                try:
                    pred = self._predict(text)
                    preds.append(pred)
                except Exception as e:
                    if raise_on_error:
                        raise e
                    else:
                        pred = None
            return preds
            