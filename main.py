
from typing import List


class Singleton(type):
    """A metaclass for singleton purpose."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args,
                **kwargs
            )
        return cls._instances[cls]


class StatsGenerator(metaclass=Singleton):
    """It generates count stats"""
    def __init__(self, lst: List[int]) -> None:
        self.lst = lst

    def less(self, number: int):
        count = len([i for i in self.lst if i > number])
        return count

    def greater(self, number: int):
        count = len([i for i in self.lst if i < number])
        return count

    def between(self, min: int, max: int):
        count = len([i for i in self.lst if i >= min and i <= max])
        return count


class DataCapture():
    def __init__(self) -> None:
        self.lst: List[int] = []

    def add(self, number: int):
        self.lst.append(number)

    def build_stats(self):
        stats = StatsGenerator(self.lst)
        return stats


capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4)  # should return 2 (only two values 3, 3 are less than 4)
stats.between(3, 6)  # should return 4 (3, 3, 4 and 6 are between 3 and 6)
stats.greater(4)  # should return 2 (6 and 9 are the only two values greater
