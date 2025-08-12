import re

ROMAN_NUMBERS = ["M", "D", "C", "L", "X", "V", "I"]
ROMAN_REGEX = re.compile(
    r"^M{0,3}(CM|CD|D?C{0,3})"
    r"(XC|XL|L?X{0,3})"
    r"(IX|IV|V?I{0,3})$"
)


def number_translator(number):
    number_string = str(number).upper()

    # Filter for invalid arabic numbers
    try:
        num_int = int(number_string)
        if num_int < 1 or num_int > 3999:
            return 'OUT OF RANGE (1-3999)'
    except ValueError:
        pass 

    is_roman_number = False
    is_arabic_number = False

    for caracter in number_string:
        if caracter in ROMAN_NUMBERS:
            is_roman_number = True
        elif caracter.isdigit():
            is_arabic_number = True
        else:
            return 'INCORRECT INPUT'

    if is_roman_number and is_arabic_number:
        return 'INCORRECT INPUT'
    elif is_roman_number:
        if not ROMAN_REGEX.fullmatch(number_string):
            return 'INVALID ROMAN NUMBER'
        return roman_to_arabic(number_string)
    else:
        return arabic_to_roman(int(number))



def arabic_to_roman(arabic_number):
    value_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    
    roman_number = ""

    for value, symbol in value_map:
        while arabic_number >= value:
            roman_number += symbol
            arabic_number -= value

    return roman_number


def roman_to_arabic(roman_number):
    value_map = {
        "M": 1000, "D": 500, "C": 100, "L": 50,
        "X": 10, "V": 5, "I": 1
    }

    arabic_number = 0
    prev_value = 0

    for char in reversed(roman_number):

        value = value_map[char]
        if value < prev_value:
            arabic_number -= value
        else:
            arabic_number += value
            prev_value = value

    return arabic_number




if __name__ == "__main__":

    test_numbers = ["MCMXCIV", "IIII", "VV", "IC", "3999", "0", 4000]

    for number in test_numbers:
        print(f"{number}: {number_translator(number)}")