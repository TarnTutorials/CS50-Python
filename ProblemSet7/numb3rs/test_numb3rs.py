# CS50P - Problem set 6 - 2022 course
# Tarn Montgomery 2024/06/20
# Test cases for the numb3rs.py program

from numb3rs import validate
import pytest

def test_format():
    assert validate("1.1.1.1") == True
    assert validate("10.10.10.10") == True
    assert validate("100.100.100.100") == True
    assert validate("cat.dog.1.100") == False
    assert validate("1.1.10000.10.50") == False
    assert validate("1.1,2,1") == False
    
def test_values():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("-1.1.1.1") == False
    assert validate("256.1.1.1") == False