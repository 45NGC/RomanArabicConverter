ROMAN_NUMBERS = ["M", "D", "C", "L", "X", "V", "I"]


def number_translator(number):
    is_roman_number = False
    is_arabic_number = False

    number_string = str(number).upper()

    for caracter in number_string:

        if caracter in ROMAN_NUMBERS:
            is_roman_number = True

        elif caracter.isdigit():
            is_arabic_number = True

        else:
            return 'INCORRECT INPUT'


    if(is_roman_number and is_arabic_number):
        return 'INCORRECT INPUT'
    
    elif(is_roman_number):
        return roman_to_arabic(number)
    
    else:
        return arabic_to_roman(number)


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
    pass
    



if __name__ == "__main__":

    test_numbers = [
        1100
    ]

    for number in test_numbers:
        print(f"{number}: {number_translator(number)}")