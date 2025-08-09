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
    final_value = ""

    for value_to_subtract in ROMAN_ARABIC.values():

        while number >= value_to_subtract:
            number -= value_to_subtract 
            final_value += ARABIC_ROMAN[value_to_subtract]
    
    return final_value



if __name__ == "__main__":

    test_numbers = [
        1100
    ]

    for number in test_numbers:
        print(f"{number}: {number_translator(number)}")