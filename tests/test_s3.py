import pytest
from src.s3 import Uploader

TESTS = [
    ("test", "prefix", "prefix/test"),
    ("test", None, "test")
]

@pytest.mark.parametrize("bucket, bucket_prefix, output", TESTS)
def test_uploader(bucket: str, bucket_prefix: str, output: str):
    uploader = Uploader(bucket=bucket, bucket_prefix=bucket_prefix)
    assert uploader.generate_key(bucket) == output
    print("TEST OK for src.uploader.Uploader()")