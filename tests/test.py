import pytest
from src import subtraction

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

def test_answer_subtraction():
    assert subtraction.subtraction(5, 3) == 2