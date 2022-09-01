import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from .annotation import Annotation

class RawText(BaseModel):
    id: str = Field(..., title="Text ID")
    text: str = Field(..., description="Online text.")
    source: str = Field(..., description="Source of the text.")
    created_at: datetime.datetime = Field(..., description="Date of creation.")
    collected_at: datetime.datetime = Field(datetime.datetime.now(), description="Date of collection.")
    is_toxic: bool = Field(None, description="Whether the text is toxic.")
    toxicity_score: float = Field(None, description="Toxicity score.")
    publisher_category: str = Field(None, description="Publisher category.")    
    annotations: Optional[List[Annotation]] = Field([], description="List of annotations.")

    @validator("toxicity_score")
    def raw_toxicity_score(cls, v):
        if v is None:
            return None
        if v < 0.0 or v > 1.0:
            raise ValueError('must be between 0.0 and 1.0')
        return v

    def __getitem__(self, item):
        return getattr(self, item)


