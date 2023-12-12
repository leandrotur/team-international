from typing import List
from bisect import bisect_left, bisect_right


class Singleton(type):
    """A metaclass for singleton purpose."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
    
class StatsGenerator(metaclass=Singleton):
    """
    A class to generate statistics based on a sorted list of integers.

    Attributes:
        lst (List[int]): A sorted list of integers.
    """

    def __init__(self, lst: List[int]) -> None:
        """
        Initialize the StatsGenerator with a list of integers and sort the list.

        Args:
            lst (List[int]): A list of integers.
        """
        self.lst = sorted(lst)

    def less(self, number: int) -> int:
        """
        Find the count of elements in the list that are less than the given number.

        Args:
            number (int): The number to compare against.

        Returns:
            int: The count of elements less than the given number.
        """
        index = bisect_left(self.lst, number)
        return index

    def greater(self, number: int) -> int:
        """
        Find the count of elements in the list that are greater than the given number.

        Args:
            number (int): The number to compare against.

        Returns:
            int: The count of elements greater than the given number.
        """
        index = bisect_right(self.lst, number)
        return len(self.lst) - index

    def between(self, min: int, max: int) -> int:
        """
        Find the count of elements in the list that are between two given numbers (inclusive).

        Args:
            min (int): The minimum number in the range.
            max (int): The maximum number in the range.

        Returns:
            int: The count of elements within the given range.
        """
        min_index = bisect_left(self.lst, min)
        max_index = bisect_right(self.lst, max)
        return max_index - min_index
