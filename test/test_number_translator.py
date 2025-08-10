import pytest
from number_translator import number_translator



def test_incorrect_input():
    assert number_translator("X5") == "INCORRECT INPUT"
    assert number_translator("AB") == "INCORRECT INPUT"



# DECIMAL TO ROMAN TEST
def test_decimal_to_roman_basic_symbols():
    assert number_translator(1) == 'I'
    assert number_translator(5) == 'V'
    assert number_translator(10) == 'X'
    assert number_translator(50) == 'L'
    assert number_translator(100) == 'C'
    assert number_translator(500) == 'D'
    assert number_translator(1000) == 'M'

def test_decimal_to_roman_addition_rule():
    assert number_translator(2) == 'II'
    assert number_translator(6) == 'VI'
    assert number_translator(15) == 'XV'
    assert number_translator(160) == 'CLX'
    assert number_translator(1600) == 'MDC'

def test_decimal_to_roman_subtraction_rule():
    assert number_translator(4) == 'IV'
    assert number_translator(9) == 'IX'
    assert number_translator(40) == 'XL'
    assert number_translator(90) == 'XC'
    assert number_translator(400) == 'CD'
    assert number_translator(900) == 'CM'

def test_decimal_to_roman_complex_numbers():
    assert number_translator(14) == 'XIV'
    assert number_translator(19) == 'XIX'
    assert number_translator(1990) == 'MCMXC'
    assert number_translator(2008) == 'MMVIII'
    assert number_translator(1666) == 'MDCLXVI'
    assert number_translator(1999) == 'MCMXCIX'
    assert number_translator(444) == 'CDXLIV'
    assert number_translator(999) == 'CMXCIX'
    assert number_translator(3999) == 'MMMCMXCIX'



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