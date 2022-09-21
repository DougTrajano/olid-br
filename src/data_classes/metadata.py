import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator


class Metadata(BaseModel):
    id: Optional[str] = Field(None, title="Unique ID for the text.")
    source: str = Field(..., title="Source/Origin")
    created_at: datetime.datetime = Field(..., title="Created at")
    collected_at: datetime.datetime = Field(..., title="Collected at")
    toxicity_score: float = Field(..., title="Toxicity score")

    # Disabled due to a bug in the ingestion data
    # category: Optional[str] = Field(None, title="Category")

    @validator("toxicity_score")
    def metadata_toxicity_score(cls, v):
        if v < 0.0 or v > 1.0:
            raise ValueError('must be between 0.0 and 1.0')
        return v

    def __getitem__(self, item):
        return getattr(self, item)