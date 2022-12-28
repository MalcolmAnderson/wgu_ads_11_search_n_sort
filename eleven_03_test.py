from eleven_03_linear_search import linear_search
# from eleven_3_binary_search import binary_search
import pytest


numbers = [2, 4, 7, 10, 11, 32, 45, 87]


def setup_function(function):
    print("\n************************************")
    function.numbers = [2, 4, 7, 10, 11, 32, 45, 87, 47]


def test_linear_search_number_not_found():
    print(numbers)
    x = linear_search(numbers, 47)
    assert x == -1
