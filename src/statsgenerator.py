from typing import List
from bisect import bisect_left, bisect_right


class StatsGenerator():
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

        Raises:
            ValueError: If the list is empty or contains non-integer elements.
        """
        if not all(isinstance(x, int) for x in lst):
            raise ValueError("List must contain only integers.")
        if not lst:
            raise ValueError("List cannot be empty.")
        self.lst = sorted(lst)

    def less(self, number: int) -> int:
        """
        Find the count of elements in the list that are less than the given number.

        Args:
            number (int): The number to compare against.

        Returns:
            int: The count of elements less than the given number.

        Raises:
            TypeError: If the number is not an integer.
        """
        if not isinstance(number, int):
            raise TypeError("The number must be an integer.")
        index = bisect_left(self.lst, number)
        return index

    def greater(self, number: int) -> int:
        """
        Find the count of elements in the list that are greater than the given number.

        Args:
            number (int): The number to compare against.

        Returns:
            int: The count of elements greater than the given number.

        Raises:
            TypeError: If the number is not an integer.
        """
        if not isinstance(number, int):
            raise TypeError("The number must be an integer.")
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

        Raises:
            TypeError: If min or max is not an integer.
            ValueError: If min is greater than max.
        """
        if not isinstance(min, int) or not isinstance(max, int):
            raise TypeError("Both min and max must be integers.")
        if min > max:
            raise ValueError("Minimum value cannot be greater than maximum value.")
        min_index = bisect_left(self.lst, min)
        max_index = bisect_right(self.lst, max)
        return max_index - min_index
