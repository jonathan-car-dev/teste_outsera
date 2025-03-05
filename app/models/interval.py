from pydantic import BaseModel

class Interval(BaseModel):
    producer: str
    interval: int
    previousWin: int
    followingWin: int