from src.datacapture import DataCapture
import pytest

@pytest.fixture
def capture():
    """Fixture para crear y devolver una nueva instancia de DataCapture."""
    def _capture(values=None):
        cap = DataCapture()
        if values:
            for value in values:
                cap.add(value)
        return cap
    return _capture

def test_less_with_repeated_numbers(capture):
    """
    Test that the 'less' method correctly counts numbers less than a given number,
    including handling repeated numbers in the data.
    """
    cap = capture([3, 3, 3])
    stats = cap.build_stats()
    assert stats.less(4) == 3

def test_greater_with_repeated_numbers(capture):
    """
    Test that the 'greater' method correctly counts numbers greater than a given number,
    including handling repeated numbers in the data.
    """
    cap = capture([3, 3, 4, 5])
    stats = cap.build_stats()
    assert stats.greater(3) == 2

def test_greater_with_boundary_values(capture):
    """
    Test that the 'greater' method accurately identifies numbers greater than a given number,
    specifically testing with boundary values in the dataset.
    """
    cap = capture([1, 2, 3])
    stats = cap.build_stats()
    assert stats.greater(1) == 2
    assert stats.greater(3) == 0

def test_greater_with_non_existent_values(capture):
    """
    Test the 'greater' method with values that do not exist in the dataset,
    ensuring it correctly returns zero when appropriate.
    """
    cap = capture([3, 6])
    stats = cap.build_stats()
    assert stats.greater(1) == 2
    assert stats.greater(10) == 0

def test_greater_with_invalid_input(capture):
    """
    Test the 'greater' method with invalid input types,
    ensuring it raises a TypeError when non-integer inputs are used.
    """
    cap = capture([2, 5])
    stats = cap.build_stats()
    with pytest.raises(TypeError):
        stats.greater("b")

def test_between_with_empty_list(capture):
    """
    Test the 'between' method with an empty dataset,
    ensuring it raises a ValueError when the dataset is empty.
    """
    capture = DataCapture()
    with pytest.raises(ValueError) as excinfo:
        stats = capture.build_stats()
    assert "List cannot be empty" in str(excinfo.value)

def test_between_with_non_existent_range(capture):
    """
    Test the 'between' method for a range of values that do not exist in the dataset,
    ensuring it returns zero when there are no numbers in the specified range.
    """
    cap = capture([2, 5])
    stats = cap.build_stats()
    assert stats.between(10, 15) == 0

def test_between_with_repeated_numbers(capture):
    """
    Test the 'between' method with repeated numbers in the dataset,
    ensuring it correctly counts the numbers within a specified range including duplicates.
    """
    cap = capture([3, 3, 4, 5])
    stats = cap.build_stats()
    assert stats.between(3, 4) == 3

def test_between_with_invalid_input(capture):
    """
    Test the 'between' method with invalid input types,
    ensuring it raises a TypeError for non-integer range limits.
    """
    cap = capture([1, 4])
    stats = cap.build_stats()
    with pytest.raises(TypeError):
        stats.between("a", 3)

    with pytest.raises(TypeError):
        stats.between(3, "b")
