from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional
from pydantic import Field

from database.models import Auditorium


class AuditoriumFilter(Filter):
    """Filtration class for auditoriums"""
    
    number: Optional[str] = Field(default=None)
    members__gte: Optional[int] = Field(default=None, alias='min_members')
    members__lte: Optional[int] = Field(default=None, alias='max_members')
    projector: Optional[bool] = Field(default=None)

    class Constants(Filter.Constants):
        model = Auditorium

    class Config:
        populate_by_name = True
