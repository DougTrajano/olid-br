import datetime
from typing import List, Any
from pydantic import BaseModel, Field, validator


class RawText(BaseModel):
    id: Any = Field(..., title="Text ID")
    text: str = Field(..., description="Online text.")
    source: str = Field(..., description="Source of the text.")
    created_at: datetime.datetime = Field(..., description="Date of creation.")
    collected_at: datetime.datetime = Field(datetime.datetime.now(), description="Date of collection.")
    is_toxic: bool = Field(None, description="Whether the text is toxic.")
    toxicity_score: float = Field(None, description="Toxicity score.")
    publisher_category: str = Field(None, description="Publisher category.")    
    
    @validator("toxicity_score")
    def raw_toxicity_score(cls, v):
        if v is None:
            return None
        if v < 0.0 or v > 1.0:
            raise ValueError('must be between 0.0 and 1.0')
        return v

class Annotator(BaseModel):
    id: str = Field(..., title="Unique ID for the text")
    annotator_id: int = Field(title="Unique ID for the annotator")
    gender: str = Field(..., title="Annotator Gender")
    age: int = Field(..., title="Annotator Age")
    education_level: str = Field(..., title="Annotator education level")
    annotator_type: str = Field(..., title="Annotator type")

    @validator("gender")
    def annotator_gender(cls, v):
        if v.lower() == "male" or v.lower() == "female":
            return v.capitalize()
        raise ValueError('must be "MALE" or "FEMALE"')

    @validator("education_level")
    def annotator_education_level(cls, v):
        levels = [
            "primary school",
            "secondary school",
            "bachelor's degree",
            "master's degree",
            "doctoral degree"
        ]

        if v.lower() in levels:
            return v.capitalize()
        raise ValueError('must be one of: {}'.format(levels))

    @validator("annotator_type")
    def check_annotator_type(cls, v):
        types = [
            "volunteer",
            "researcher",
            "contract worker"
        ]

        if v.lower() in types:
            return v.capitalize()
        raise ValueError('must be one of: {}'.format(types))

class ProcessedText(BaseModel):
    id: Any = Field(..., title="Unique ID")
    text: str = Field(..., title="Anonymized text")
    is_offensive: str = Field(..., title="Offensive label")
    is_targeted: str = Field(..., title="Targeted")
    targeted_type: str = Field(None, title="Targeted type")
    toxic_spans: List[int] = Field(None, title="Toxic spans")
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

class Metadata(BaseModel):
    id: str = Field(..., title="Unique ID for the text.")
    source: str = Field(..., title="Source/Origin")
    created_at: datetime.datetime = Field(..., title="Created at")
    collected_at: datetime.datetime = Field(..., title="Collected at")
    toxicity_score: float = Field(..., title="Toxicity score")
    category: str = Field(None, title="Category")

    @validator("toxicity_score")
    def metadata_toxicity_score(cls, v):
        if v < 0.0 or v > 1.0:
            raise ValueError('must be between 0.0 and 1.0')
        return v
