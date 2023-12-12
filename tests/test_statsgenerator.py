from src.datacapture import DataCapture
import pytest

# Tests for less
def test_less_with_repeated_numbers():
    capture = DataCapture()
    capture.add(3)
    capture.add(3)
    capture.add(3)
    stats = capture.build_stats()
    assert stats.less(4) == 3

# Tests for greater
def test_greater_with_repeated_numbers():
    capture = DataCapture()
    capture.add(3)
    capture.add(3)
    capture.add(4)
    capture.add(5)
    stats = capture.build_stats()
    assert stats.greater(3) == 2

def test_greater_with_boundary_values():
    capture = DataCapture()
    capture.add(1)
    capture.add(2)
    capture.add(3)
    stats = capture.build_stats()
    assert stats.greater(1) == 2
    assert stats.greater(3) == 0

def test_greater_with_non_existent_values():
    capture = DataCapture()
    capture.add(3)
    capture.add(6)
    stats = capture.build_stats()
    assert stats.greater(1) == 2
    assert stats.greater(10) == 0

def test_greater_with_invalid_input():
    capture = DataCapture()
    capture.add(2)
    capture.add(5)
    stats = capture.build_stats()
    with pytest.raises(TypeError):
        stats.greater("b")

# Tests for between
def test_between_with_empty_list():
    capture = DataCapture()
    with pytest.raises(ValueError) as excinfo:
        stats = capture.build_stats()
    assert "List cannot be empty" in str(excinfo.value)

def test_between_with_non_existent_range():
    capture = DataCapture()
    capture.add(2)
    capture.add(5)
    stats = capture.build_stats()
    assert stats.between(10, 15) == 0

def test_between_with_repeated_numbers():
    capture = DataCapture()
    capture.add(3)
    capture.add(3)
    capture.add(4)
    capture.add(5)
    stats = capture.build_stats()
    assert stats.between(3, 4) == 3

def test_between_with_invalid_input():
    capture = DataCapture()
    capture.add(1)
    capture.add(4)
    stats = capture.build_stats()
    with pytest.raises(TypeError):
        stats.between("a", 3)

    with pytest.raises(TypeError):
        stats.between(3, "b")
