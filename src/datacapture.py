from typing import List
from src.statsgenerator import StatsGenerator


class DataCapture():
    def __init__(self) -> None:
        self.lst: List[int] = []

    def add(self, number: int):
        self.lst.append(number)

    def build_stats(self):
        stats = StatsGenerator(self.lst)
        return stats
