from src.processing.text import (
    get_toxic_substrings,
    get_idx_substrings
)

TESTS = [
    {
        "text": "USER kkkk eu espero que esse lula ganhe e termine de acaba com brasil é só o que vocês merece mesmo , vou esta de camarote assistindo a merda que vocês fez",
        "toxic_spans": [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155]
    },
    {
        "text": "DESGRAÇA CARAIO BUCETA, É HOJE PORRA",
        "toxic_spans": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    }
]

def test_get_toxic_substrings():
    for test in TESTS:
        toxic_substrings = get_toxic_substrings(test["text"], test["toxic_spans"])
        assert type(toxic_substrings) == list

def test_get_idx_substrings():
    for test in TESTS:
        toxic_substrings = get_toxic_substrings(test["text"], test["toxic_spans"])
        idx_substrings = get_idx_substrings(test["text"], toxic_substrings)
        assert type(idx_substrings) == list