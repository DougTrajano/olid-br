import os
import json
import boto3
import logging
from typing import Dict, Any

_logger = logging.getLogger()


class Uploader(object):
    def __init__(self, bucket: str, bucket_prefix: str = None):
        self.bucket_name = bucket
        self.bucket_prefix = bucket_prefix
        
        _logger.debug(f"Uploader initialized with bucket: {bucket}")

    def generate_key(self, key: str):
        """
        Concatenate key prefix and key.

        Arguments:
            key (str): Key to be uploaded to S3

        Returns:
            str: Key to be uploaded to S3
        """
        if self.bucket_prefix:
            return f"{self.bucket_prefix}/{key}"
        else:
            return key

    def upload_sts(self, role_arn: str, session_name: str, key: str, data: dict):
        """
        Assume a role in order to upload to S3.

        Arguments:
            role_arn (str): ARN of the role to assume.
            session_name (str): Name of the session.
            key (str): Key to be uploaded to S3.
            data (dict): Data to be uploaded to S3.

        Returns:
            dict: Response from the S3 service.
        """
        _logger.debug("Uploading to S3 using STS.")

        # Create a client using the role and temp credentials
        sts_client = boto3.client("sts")

        response = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=session_name
        )

        session = boto3.Session(
            aws_access_key_id=response["Credentials"]["AccessKeyId"],
            aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
            aws_session_token=response["Credentials"]["SessionToken"]
        )

        # Prepare key
        key = self.generate_key(key)

        # Convert dict to json serializable
        data = json.dumps(data).encode('UTF-8')

        # Upload to S3
        s3 = session.resource("s3")
        obj = s3.Object(self.bucket_name, key)
        result = obj.put(Body=data)

        _logger.debug("S3 upload completed.")

        return result

    def upload_aksk(self, access_key: str, secret_key: str, key: str, data: dict):
        """
        Upload to S3 using AKSK.

        Arguments:
            access_key (str): Access key to be used.
            secret_key (str): Secret key to be used.
            key (str): Key to be uploaded to S3.
            data (dict): Data to be uploaded to S3.

        Returns:
            dict: Response from the S3 service.
        """
        _logger.debug("Uploading to S3 using access key and secret key.")

        # Prepare key
        key = self.generate_key(key)

        # Convert dict to json serializable
        data = json.dumps(data, ensure_ascii=False)

        # Upload to S3
        s3 = boto3.resource("s3",
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key)

        obj = s3.Object(self.bucket_name, key)
        result = obj.put(Body=data)

        _logger.debug("S3 upload completed.")
        
        return result
        

def get_json_from_s3(bucket: str, key: str,
                     aws_access_key_id: str = None,
                     aws_secret_access_key: str = None) -> Dict[Any, Any]:
    """
    Get the json from the s3 bucket.

    Args:
    - bucket: The name of the bucket.
    - key: The key of the json file.
    - aws_access_key_id: The access key id of the aws account.
    - aws_secret_access_key: The secret access key of the aws account.

    If aws_access_key_id and aws_secret_access_key are not provided, it will use the env vars.
    Returns:
    - The json file.
    """
    _logger.debug(f"Getting json from s3 bucket: {bucket} and key: {key}")

    if aws_access_key_id is None:
        aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
    if aws_secret_access_key is None:
        aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]

    # Initialize the boto3 client
    boto3.Session(aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

    s3 = boto3.resource("s3")
    obj = s3.Object(bucket, key)

    result = json.loads(obj.get()["Body"].read().decode("utf-8"))

    _logger.debug(f"Returning json with size: {len(result)}")
    return result
