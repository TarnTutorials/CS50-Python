# CS50P - Problem set 5 - 2022 course
# Tarn Montgomery 2024/06/14
# Tests the bank.py file to ensure it is outputting correctly.

import bank
import pytest

#Test to ensure case is working correctly
def test_case():
    assert bank.value("Hello") == 0 
    assert bank.value("hello") == 0 
    assert bank.value("Howdie") == 20 
    assert bank.value("howdie") == 20 
    assert bank.value("what's up") == 100 
    assert bank.value("What's up") == 100 

#Test to ensure numbers are not causing issues
def test_numbers():
    assert bank.value("23Hello") == 0 
    assert bank.value("H3ll0") == 20 
    assert bank.value("hello0123") == 0 

#Test to ensure punctuation are not causing issues
def test_punctuation():
    assert bank.value(".hello") == 0
    assert bank.value("howdie.") == 20
    assert bank.value("hello.") == 0

#Test to ensure multiple words are not causing issues
def test_multiwords():
    assert bank.value("Mr Jenkins, Hello") == 0
    assert bank.value("Hello, Dr.Hyde") == 0
    assert bank.value("Hyde, Hello, nice to see you again.") == 0 

    #Test to ensure multiple words are not causing issues
def test_blackspace():
    assert bank.value("   Mr Jenkins, Hello") == 0
    assert bank.value("   Hello, Dr.Hyde") == 0
    assert bank.value("  Hyde,    Hello, nice to see you again.    ") == 0
    

