import pytest
from src.number_translator import number_translator


# ROMAN TO DECIMAL TEST
def test_roman_to_decimal_basic_symbols():
    assert number_translator('I') == 1
    assert number_translator('V') == 5
    assert number_translator('X') == 10
    assert number_translator('L') == 50
    assert number_translator('C') == 100
    assert number_translator('D') == 500
    assert number_translator('M') == 1000

def test_roman_to_decimal_addition_rule():
    assert number_translator('II') == 2
    assert number_translator('VI') == 6
    assert number_translator('XV') == 15
    assert number_translator('CLX') == 160
    assert number_translator('MDC') == 1600

def test_roman_to_decimal_subtraction_rule():
    assert number_translator('IV') == 4
    assert number_translator('IX') == 9
    assert number_translator('XL') == 40
    assert number_translator('XC') == 90
    assert number_translator('CD') == 400
    assert number_translator('CM') == 900

def test_roman_to_decimal_complex_numbers():
    assert number_translator('XIV') == 14
    assert number_translator('XIX') == 19
    assert number_translator('MCMXC') == 1990
    assert number_translator('MMVIII') == 2008
    assert number_translator('MDCLXVI') == 1666
    assert number_translator('MCMXCIX') == 1999
    assert number_translator('CDXLIV') == 444
    assert number_translator('CMXCIX') == 999
    assert number_translator('MMMCMXCIX') == 3999