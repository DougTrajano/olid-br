from src.language_detector import LanguageDetector

def test_language_detector():
    """Test the language detector class."""
    text = "Este é um texto em português."
    language_detector = LanguageDetector()
    assert language_detector.predict(text) == "pt"
    assert language_detector.predict([text]) == ["pt"]