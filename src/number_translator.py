ROMAN_ARABIC = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}

ARABIC_ROMAN = {
    1000: "M",
    500: "D",
    100: "C",
    50: "L",
    10: "X",
    5: "V",
    1: "I"
}

def number_translator(number):
    is_roman_number = False
    is_arabic_number = False

    number_string = str(number).upper()

    for caracter in number_string:

        if caracter in ROMAN_ARABIC.keys():
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
    final_value = ""

    for value_to_subtract in ROMAN_ARABIC.values():

        while arabic_number >= value_to_subtract:
            arabic_number -= value_to_subtract 
            final_value += ARABIC_ROMAN[value_to_subtract]
    
    return final_value


def roman_to_arabic(roman_number):
    pass
    



if __name__ == "__main__":

    test_numbers = [
        1100
    ]

    for number in test_numbers:
        print(f"{number}: {number_translator(number)}")