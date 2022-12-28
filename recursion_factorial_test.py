from recursion_factorial import nfact
from pytest import raises


def test_1_should_return_1():
    assert 1 == nfact(1), "identity, 1 should return 1"


def test_2_should_return_2():
    assert 2 == nfact(2), "fail, nfact(2) should have returned 2"


def test_4_should_return_24():
    assert 24 == nfact(4), "fail, nfact(4) should have returned 24"


def test_negative_numbers_should_fail():
    with raises(ValueError, match="Negative numbers is not a valid input for nfact."):
        # with raises(ValueError):
        nfact(-2)
