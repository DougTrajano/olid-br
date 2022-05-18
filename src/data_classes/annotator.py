from typing import Optional
from pydantic import BaseModel, Field, validator

class Annotator(BaseModel):
    id: Optional[str] = Field(None, title="Unique ID for the text")
    annotator_id: int = Field(..., title="Unique ID for the annotator")
    gender: str = Field(..., title="Annotator Gender")
    year_of_birth: int = Field(..., title="Year of birth of the annotator")
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
            "high school",
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