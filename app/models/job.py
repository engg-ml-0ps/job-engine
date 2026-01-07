from pydantic import BaseModel, Field
from typing import List, Optional


class JobCreate(BaseModel):
    name: str = Field(..., min_length=3)
    description: str = Field(..., min_length=10)
    industry: str
    keywords: List[str]


class Job(JobCreate):
    id: int
