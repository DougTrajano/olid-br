import re
import json
from typing import List, Union

def get_toxic_substrings(text: str, spans: Union[List[int], str]) -> List[str]:
    """
    Extract string words based on a list of spans.

    Args:
    - text: The text to extract words from.
    - spans: A list of spans to extract words from.

    Returns:
    - A list of words extracted from the text.
    """
    def format_substring(substring: str):
        return " ".join("".join(substring).split())

    def format_word(word: str):
        word = re.sub(r"[^\w\s]", "", word)
        return word.strip()

    def fix_incomplete_words(text: str, words: List[str]):
        adjusted_words = []
        for text_word in text.split():
            for word in words:
                if len(word.split()) == 1:
                    if word in text_word:
                        adjusted_words.append(format_word(text_word))
                elif len(word.split()) > 1:
                    first_word = word.split()[0]
                    if first_word in text_word:
                        first_word = format_word(text_word)
                        adjusted_word = first_word + " " + " ".join(word.split()[1:])
                        adjusted_words.append(adjusted_word)
        return adjusted_words

    if isinstance(spans, str):
        spans = json.loads(spans)

    delimiter = None
    words = []
    chars = []
    for i in range(len(text)):
        if i in spans:
            if delimiter is None:
                delimiter = i
            else:
                delimiter += 1
            chars.append(text[i])
        else:
            chars.append(" ")

        if delimiter is not None and i != delimiter:
            words.append(format_substring(chars))
            chars = []
            delimiter = None

    if len(chars) > 0:
        words.append(format_substring(chars))
        
    words = [w.strip() for w in words if w not in [" ", ""]]
    words = fix_incomplete_words(text, words)

    return words

def get_idx_substrings(text: str, substrings: List[str]) -> List[int]:
    """
    Get the indexes of all substrings in text.

    Args:
    - text: the text to search in
    - substrings: the substrings to search for

    Returns:
    - a list of indexes of all substrings in text
    """
    idx_substrings = []
    for substring in substrings:
        idx_substrings.extend(
            [(m.start(), m.end()) for m in re.finditer(substring, text)]
        )
    return idx_substrings