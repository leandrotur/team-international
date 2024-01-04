from typing import List

class StatsGenerator():
    """
    A class to generate statistics based on a sorted list of integers.

    Attributes:
        lst (List[int]): A sorted list of integers.
        less_counts (List[int]): Precomputed counts of elements less than or equal to each index.
        greater_counts (List[int]): Precomputed counts of elements greater than or equal to each index.
    """

    def __init__(self, lst: List[int]) -> None:
        """
        Initialize the StatsGenerator with a list of integers and sort the list.

        Args:
            lst (List[int]): A list of integers.

        Raises:
            ValueError: If the list contains non-integer elements.
        """
        if any(not isinstance(x, int) for x in lst):
            raise ValueError("List must contain only integers.")
        if not lst:
            raise ValueError("List cannot be empty.")
        
        self.lst = sorted(lst)
        self.less_counts = self._compute_less_counts()
        self.greater_counts = self._compute_greater_counts()

    def _compute_less_counts(self) -> List[int]:
        """
        Compute the counts of elements less than or equal to each index.

        Returns:
            List[int]: List of counts.
        """
        count = 0
        less_counts = []
        for num in self.lst:
            count += 1
            less_counts.append(count)
        return less_counts

    def _compute_greater_counts(self) -> List[int]:
        """
        Compute the counts of elements greater than or equal to each index.

        Returns:
            List[int]: List of counts.
        """
        count = 0
        greater_counts = []
        for num in reversed(self.lst):
            count += 1
            greater_counts.insert(0, count)
        return greater_counts

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
        index = self._find_index(number)
        return self.less_counts[index] if index >= 0 else 0

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
        index = self._find_index(number)
        return len(self.lst) - self.less_counts[index] if index >= 0 else 0

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

        min_index = self._find_index(min - 1)
        max_index = self._find_index(max)
        return max_index - min_index

    def _find_index(self, number: int) -> int:
        """
        Find the index of the largest element less than or equal to the given number.

        Args:
            number (int): The number to compare against.

        Returns:
            int: The index of the largest element less than or equal to the given number.
        """
        left, right = 0, len(self.lst) - 1
        index = -1

        while left <= right:
            mid = (left + right) // 2
            if self.lst[mid] <= number:
                index = mid
                left = mid + 1
            else:
                right = mid - 1

        return index

