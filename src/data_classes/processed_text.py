from typing import List, Any, Optional
from pydantic import BaseModel, Field, validator

class ProcessedText(BaseModel):
    id: Any = Field(..., title="Unique ID")
    text: str = Field(..., title="Anonymized text")
    is_offensive: str = Field(..., title="Offensive label")
    is_targeted: str = Field(..., title="Targeted")
    targeted_type: Optional[str] = Field(None, title="Targeted type")
    toxic_spans: Optional[List[int]] = Field(None, title="Toxic spans")
    health: bool = Field(..., title="Health label")
    ideology: bool = Field(..., title="Ideology")
    insult: bool = Field(..., title="Insult")
    lgbtqphobia: bool = Field(..., title="LGBTQphobia")
    other_lifestyle: bool = Field(..., title="Other-Lifestyle")
    physical_aspects: bool = Field(..., title="Physical-Aspects")
    profanity_obscene: bool = Field(..., title="Profanity or Obscene")
    racism: bool = Field(..., title="Racism")
    religious_intolerance: bool = Field(..., title="Religious Intolerance")
    sexism: bool = Field(..., title="Sexism")
    xenophobia: bool = Field(..., title="Xenophobia")

    @validator("is_offensive")
    def processed_is_offensive(cls, v):
        if v == "OFF" or v == "NOT":
            return v
        raise ValueError('must be "OFF" or "NOT"')
    
    @validator("is_targeted")
    def processed_is_targeted(cls, v):
        if v == "TIN" or v == "UNT":
            return v
        raise ValueError('must be "TIN" or "UNT"')
    
    @validator("targeted_type")
    def processed_targeted_type(cls, v):
        if v is None:
            return None

        if v == "IND" or v == "GRP" or v == "OTH":
            return v
        raise ValueError('must be "IND", "GRP" or "OTH"')
    
    @validator("toxic_spans")
    def processed_toxic_spans(cls, v):
        if v is None:
            return None

        for i in v:
            if not isinstance(i, int):
                raise ValueError('must be int')
            if i < 0:
                raise ValueError('must be positive')
        return v

    def __getitem__(self, item):
        return getattr(self, item)
        