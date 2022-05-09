import json
import boto3
import logging
from typing import Dict, Any, List, Union
from pandas import DataFrame
from io import StringIO

_logger = logging.getLogger()


class Bucket(object):
    def __init__(self, bucket: str):
        """Initialize the bucket.

        Parameters:
        - bucket (str): The name of the bucket.
        """
        self.bucket_name = bucket
        _logger.debug(f"Initialized Bucket: {self.bucket_name}.")

    def get_session_from_sts(self, role_arn: str, session_name: str):
        """Get a session from STS.

        Args:
        - role_arn (str): The ARN of the role to assume.
        - session_name (str): The name of the session.
        """
        # Create a client using the role and temp credentials
        sts_client = boto3.client("sts")

        response = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=session_name)

        session = boto3.Session(
            aws_access_key_id=response["Credentials"]["AccessKeyId"],
            aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
            aws_session_token=response["Credentials"]["SessionToken"])

        self.s3 = session.resource("s3")

    def get_session_from_aksk(self, access_key: str, secret_key: str):
        """Get a session from Access Key and Secret Key.

        Args:
        - access_key (str): The access key.
        - secret_key (str): The secret key.
        """
        self.s3 = boto3.resource(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key)

    def upload_json(self, data: Union[Dict[Any, Any], List[Dict[Any, Any]]], key: str):
        """Upload a dictionary or list of dictionaries to S3 as JSON.

        Args:
        - data (dict): Data to be uploaded to S3.
        - key (str): Key to be uploaded to S3.

        Returns:
        - Response from the boto3 S3 service.
        """
        _logger.debug("Uploading file to S3.")

        # Convert dict to json serializable
        data = json.dumps(data).encode('UTF-8')

        # Upload to S3
        obj = self.s3.Object(self.bucket_name, key)
        result = obj.put(Body=data)

        _logger.debug("S3 upload completed.")
        return result

    def upload_csv(self, data: DataFrame, key: str):
        """Upload a file to S3.

        Args:
        - data (DataFrame): Data to be uploaded to S3.
        - key (str): Key to be uploaded to S3.

        Returns:
        - Response from the boto3 S3 service.
        """
        _logger.debug("Uploading file to S3.")

        csv_buffer = StringIO()

        # Write to buffer
        data.to_csv(csv_buffer, index=False, encoding="utf-8")

        obj = self.s3.Object(self.bucket_name, key)
        result = obj.put(Body=csv_buffer.getvalue())

        _logger.debug("S3 upload completed.")
        return result


    def download_json(self, key: str):
        """Download a JSON file from S3.

        Args:
        - key (str): The key of the file to download.

        Returns:
        - The contents of the file.
        """
        _logger.debug("Downloading from S3 using STS.")
        
        # Download from S3
        obj = self.s3.Object(self.bucket_name, key)
        result = json.loads(obj.get()["Body"].read().decode("utf-8"))

        _logger.debug(f"Returning json with size: {len(result)}")
        return result       
