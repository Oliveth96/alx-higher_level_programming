#!/usr/bin/python3
def roman_to_int(roman_string):
    #for fail check, none, not a string
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    
    #I created a dictionary for the roman numerals
    roman_dictionary = {
        'I': 1,
        'IV': 4,
        'IX': 9,
        'X': 10,
        'L': 50,
        'C': 500,
        'D': 500,
        'M': 1000
    }

    result = 0
    tem = list(roman_string)

    #to concatenate 4s and 9s
    if len(tem) > 1:
        ivix = 0
        for i in tem:
            try:
                if tem[ivix] == 'I' and tem[ivix + 1] == 'V':
                    tem[ivix:ivix + 2] = [''.join(tem[ivix:ivix + 2])]
            except IndexError:
                pass
            try:
                if tem[ivix] == 'I' and tem[ivix + 1] == 'X':
                    tem[ivix:ivix + 2] = [''.join(tem[ivix:ivix + 2])]
            except IndexError:
                pass
            ivix += 1

        #Search my roman dictionary for correct numbers and  add them together
        for key, value in roman_dictionary.items():
            for index in tem:
                if index == key:
                    result += value
        return result
