import pytest
from file1 import add_five
from file1 import greet

def test_add_five():
    assert add_five(5) == 10

def test_add_negative():
    assert add_five(-2) == 3

def test_add_float():
    assert add_five(0.5) == 5.5


def greet_name():
    assert greet('vipal') == "Hello, vipal"

def greet_name():
    assert greet('VIPAL') == "Hello, VIPAL"