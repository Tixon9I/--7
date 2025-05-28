from app.main import calculate_rectangle_area
import pytest

def test_calculate_rectangle_area():
    assert calculate_rectangle_area(4, 5) == 20
    assert calculate_rectangle_area(10, 2) == 20
    assert calculate_rectangle_area(1, 1) == 1

def test_invalid_input():
    with pytest.raises(ValueError):
        calculate_rectangle_area(-1, 5)
    with pytest.raises(ValueError):
        calculate_rectangle_area(0, 10)