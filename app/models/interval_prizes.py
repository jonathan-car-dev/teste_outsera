from typing import List
from pydantic import BaseModel
from .interval import Interval


class IntervalPrizes(BaseModel):
    min: List[Interval]
    max: List[Interval]
