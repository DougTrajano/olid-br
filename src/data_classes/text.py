import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from .annotation import Annotation


class Metadata(BaseModel):
    source: str = Field(..., title="Source/Origin")
    created_at: datetime.datetime = Field(..., title="Created at")
    collected_at: datetime.datetime = Field(..., title="Collected at")
    toxicity_score: float = Field(..., title="Toxicity score")
    category: Optional[str] = Field(None, title="Category")

    @validator("toxicity_score")
    def metadata_toxicity_score(cls, v):
        if v < 0.0 or v > 1.0:
            raise ValueError('must be between 0.0 and 1.0')
        return v

    def __getitem__(self, item):
        return getattr(self, item)

class Text(BaseModel):
    id: str = Field(..., title="Unique ID")
    text: str = Field(..., title="Anonymized text")
    metadata: Metadata = Field(..., title="Metadata")
    annotations: List[Annotation] = Field([], title="Annotations")