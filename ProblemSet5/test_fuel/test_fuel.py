# CS50P - Problem set 5 - 2022 course
# Tarn Montgomery 2024/06/14
# Tests the fuel.py file to ensure it is outputting correctly.

import pytest
from fuel import gauge, convert

#Test section for convert

#Test for Value Error of convert
def test_value_error():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("1/1") == 100
    with pytest.raises(ValueError):  
        assert convert("Cat/Dog") 
        assert convert("1/2/3")
        assert convert("3/2")
        assert convert("100/cat")
    
#Test for Zero Error of convert
def test_zero_error():
    assert gauge(10) == "10%"
    with pytest.raises(ZeroDivisionError):  
        assert convert("24/0") 

#Test section for Guage 
#Test for value Error of guage
def test_value_error():
    assert gauge(10) == "10%"
    with pytest.raises(ValueError):  
        assert gauge("test") 
  
#Test for final output
def test_output():
    assert gauge(10) == "10%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"