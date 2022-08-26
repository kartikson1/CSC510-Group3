import pytest
import src

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

def test_answer_subtraction():
    assert src.subtraction(5, 3) == 2