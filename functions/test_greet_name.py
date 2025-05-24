import pytest
from file1 import greet

def test_greet_name_lowercase():
    assert greet('vipal') == "Hello, vipal!"

def test_greet_name_uppercase():
    assert greet('VIPAL') == "Hello, VIPAL!"