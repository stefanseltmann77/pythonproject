# Dummy file for some basic ETL class
import logging
from typing import List


class BasicEtl:
    logger: logging.Logger

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run_etl(self, some_data: List[int]) -> int:
        self.logger.info("Running ETL")
        return sum(some_data)
