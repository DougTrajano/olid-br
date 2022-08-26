import re
import json
from typing import Any, List, Union

def get_toxic_substrings(text: str, spans: Union[List[int], str]) -> List[str]:
    """Get the toxic substrings in text given the spans.

    Args:
    - text: The text to extract words from.
    - spans: A list of spans to extract words from.

    Returns:
    - A list of words extracted from the text.
    """
    def format_chars(chars: List[Any]) -> str:
        return " ".join("".join(chars).split()).strip()

    def format_substring(substring: str):
        return re.sub(r"[^\w\s]", "", substring).strip()

    def fix_incomplete_substrings(text: str, substrings: List[str]):
        adjusted_substrings = []
        for substring in substrings:
            if len(substring.split()) == 1:
                for word_text in text.split():
                    if substring in word_text:
                        adjusted_substrings.append(format_substring(word_text))
                        break
            elif len(substring.split()) > 1:
                first_word = substring.split()[0]
                last_word = substring.split()[-1]

                for word_text in text.split():
                    if first_word in word_text:
                        first_word = format_substring(word_text)
                    if last_word in word_text:
                        last_word = format_substring(word_text)

                    adjusted_substring = [first_word] + substring.split()[1:-1] + [last_word]
                    adjusted_substrings.append(" ".join(adjusted_substring))
                    break
                
        return adjusted_substrings

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
            words.append(format_chars(chars))
            chars = []
            delimiter = None

    if len(chars) > 0:
        words.append(format_chars(chars))

    words = [w.strip() for w in words if w not in [" ", ""]]
    words = fix_incomplete_substrings(text, words)
    return words

def get_idx_substrings(text: str, substrings: List[str]) -> List[int]:
    """Get the indexes of all substrings in text.

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