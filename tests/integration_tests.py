import os
import unittest
import requests
from dotenv import load_dotenv

from app.models import IntervalPrizes


class TestDataIntegrity(unittest.TestCase):
    def test_data(self):
        load_dotenv()
        response = requests.get(os.getenv('API_URL') + '/movies/producer_interval_reward')
        response_data = response.json()
        interval_prizes = IntervalPrizes.model_validate(response_data)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(interval_prizes.min), 1)
        self.assertEqual(interval_prizes.min[0].producer, "Joel Silver")
        self.assertEqual(interval_prizes.min[0].interval, 1)
        self.assertEqual(interval_prizes.min[0].previousWin, 1990)
        self.assertEqual(interval_prizes.min[0].followingWin, 1991)

        self.assertEqual(len(interval_prizes.max), 1)
        self.assertEqual(interval_prizes.max[0].producer, "Matthew Vaughn")
        self.assertEqual(interval_prizes.max[0].interval, 13)
        self.assertEqual(interval_prizes.max[0].previousWin, 2002)
        self.assertEqual(interval_prizes.max[0].followingWin, 2015)