import pytest
from src.s3 import Bucket

def test_bucket():
    bucket_name = "test-bucket"
    bucket = Bucket(bucket=bucket_name)
    
    assert type(bucket) == Bucket
    assert bucket.bucket_name == bucket_name
    print("TEST OK for src.s3.Bucket()")