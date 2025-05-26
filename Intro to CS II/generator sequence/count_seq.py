"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Nov. 15, 2022
Description: Returns frequency-digit generator function sequence
as integers in strings
"""

def count_seq():
    """Takes no arguments,
    returns frequency-digit sequence"""
    num = str(2)

    if len(num) < 2:
        yield num

    while num:
        array = list(num)
        num = ""

        for (val, char) in enumerate(array):
            cont = val + 1
            if cont < len(array):
                while array[cont] in array[val]:
                    array[val] += array[cont]
                    del array[cont]

        for (val, char) in enumerate(array):
            array[val] = str(len(char)) + str(char[0])
            num += array[val]

        yield num
