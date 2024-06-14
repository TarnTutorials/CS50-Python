# CS50P - Problem set 5 - 2022 course
# Tarn Montgomery 2024/06/14
# Tests the plates.py file to ensure it is outputting correctly.

from plates import is_valid


def test_length():
    assert is_valid("toolong") == False
    assert is_valid("s") == False
    assert is_valid("Test") == True
    
def test_alphabet():
    assert is_valid("AB") == True
    assert is_valid("A") == False
    assert is_valid("CD") == True
    assert is_valid("12") == False
    assert is_valid("!@") == False
    assert is_valid("1A") == False
    assert is_valid("!A") == False
    
def test_numbers():
    assert is_valid("AB") == True
    assert is_valid("A2D") == False
    assert is_valid("CD12") == True
    assert is_valid("12DX") == False
    assert is_valid("AS123") == True
    assert is_valid("AS1AS") == False
    assert is_valid("DC2134") == True
    
def test_zero():
    assert is_valid("AB") == True
    assert is_valid("A0D") == False
    assert is_valid("CD10") == True
    assert is_valid("10DX") == False
    assert is_valid("AS1230") == True
    assert is_valid("AS012") == False
    assert is_valid("DC2034") == True
    
def test_symbols():
    assert is_valid("AB!") == False
    assert is_valid("A0D!") == False
    assert is_valid("CD10!") == False
    assert is_valid("10DX!") == False
    assert is_valid("AS123") == True
    assert is_valid("AS0!2") == False
    assert is_valid("!DC234") == False


