# CS50P - Problem set 5 - 2022 course
# Tarn Montgomery 2024/06/14
# Tests the twttr.py file to ensure it is outputting correctly.

from twttr import shorten

def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("my name is tom") == "my nm s tm"
    assert shorten("CaPiTALs") ==  "CPTLs"
    assert shorten("!!SymBOLS!___    !") == "!!SymBLS!___    !"
    assert shorten("NUMB3RS T3ST") == "NMB3RS T3ST"
    
