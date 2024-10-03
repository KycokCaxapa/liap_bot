from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional
from pydantic import Field

from database.models import Equipment


class EquipmentFilter(Filter):
    """Filtration class for equipment"""

    thing: Optional[str] = Field(default=None)
    amount__gte: Optional[int] = Field(default=None, alias='min_amount')

    class Constants(Filter.Constants):
        model = Equipment
    
    class Config:
        populate_by_name = True
