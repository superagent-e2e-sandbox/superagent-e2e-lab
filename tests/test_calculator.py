"""Tests for the integer calculator: positive, negative and zero operands."""

import pytest

from calculator import add, subtract


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-2, -3, -5),
        (-5, 3, -2),
        (0, 7, 7),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (-5, -3, -2),
        (3, 5, -2),
        (0, 7, -7),
        (7, 0, 7),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
