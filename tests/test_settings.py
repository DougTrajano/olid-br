import os

os.environ["LOG_LEVEL"] = "DEBUG"
os.environ["PERSPECTIVE_API_KEY"] = "PERSPECTIVE-API-KEY"
os.environ["TWITTER_CONSUMER_KEY"] = "TWITTER-CONSUMER-KEY"
os.environ["TWITTER_CONSUMER_SECRET"] = "TWITTER-CONSUMER-SECRET"
os.environ["TWITTER_ACCESS_TOKEN"] = "TWITTER-ACCESS-TOKEN"
os.environ["TWITTER_ACCESS_TOKEN_SECRET"] = "TWITTER-ACCESS-TOKEN-SECRET"
os.environ["TWITTER_MAX_TWEETS"] = "200"
os.environ["AWS_S3_BUCKET"] = "toxicity-crawler"
os.environ["AWS_ACCESS_KEY_ID"] = "AWS-ACCESS-KEY-ID"
os.environ["AWS_SECRET_ACCESS_KEY"] = "AWS-SECRET-ACCESS-KEY"

from src.settings import AppSettings

def test_settings():
    settings = AppSettings()
    assert type(settings) == AppSettings
    print("TEST OK for src.settings.AppSettings()")