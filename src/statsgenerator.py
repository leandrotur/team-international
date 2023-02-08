
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
    """Main function is to generate stats"""
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
