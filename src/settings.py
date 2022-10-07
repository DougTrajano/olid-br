from pydantic import BaseSettings, Field

class AppSettings(BaseSettings):
    AWS_ACCESS_KEY_ID: str = Field(None, description="AWS Access Key ID")
    AWS_S3_BUCKET: str = Field(..., description="AWS S3 Bucket")
    AWS_S3_BUCKET_PREFIX: str = Field("raw", description="AWS S3 Bucket prefix")
    AWS_SECRET_ACCESS_KEY: str = Field(None, description="AWS Secret Access Key")
    FILTER_TOXIC_COMMENTS: bool = Field(True, description="Filter toxic comments")
    HUGGINGFACE_HUB_TOKEN: str = Field(None, description="HuggingFace Hub Token")
    KAGGLE_KEY: str = Field(None, description="Kaggle API Key")
    KAGGLE_USERNAME: str = Field(None, description="Kaggle Username")
    LOG_LEVEL: str = Field("INFO", description="Logging Level")
    PERSPECTIVE_API_KEY: str = Field(None, description="Perspective API Key")
    PERSPECTIVE_THRESHOLD: float = Field(0.7, description="Perspective toxicity threshold")
    TWITTER_ACCESS_TOKEN: str = Field(None, description="Twitter Access Token")
    TWITTER_ACCESS_TOKEN_SECRET: str = Field(None, description="Twitter Access Token Secret")
    TWITTER_CONSUMER_KEY: str = Field(None, description="Twitter Consumer Key")
    TWITTER_CONSUMER_SECRET: str = Field(None, description="Twitter Consumer Secret")
    TWITTER_MAX_TWEETS: int = Field(100, description="Max tweets to fetch")
    YOUTUBE_API_KEY: str = Field(None, description="Youtube API Key")
    YOUTUBE_MAX_COMMENTS: int = Field(50, description="Max comments per video")
    YOUTUBE_MAX_COMMENTS_PER_VIDEO: int = Field(None, description="Max comments per video")