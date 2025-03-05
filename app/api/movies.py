from fastapi import APIRouter
from app.models import IntervalPrizes
from app.services import retrieve_producer_interval_reward

router = APIRouter()

@router.get('/producer_interval_reward')
def producer_interval_reward() -> IntervalPrizes:
    return retrieve_producer_interval_reward()