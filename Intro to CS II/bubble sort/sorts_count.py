"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Oct. 18, 2022
Description: Compares comparisons, exchanges between bubble and insertion sort algorithms
"""

def bubble_count(array):
    """Bubble sorts array in ascending order,
    counts comparisons and exchanges"""
    compare, exchange = 0, 0
    for pass_num in range(len(array) - 1):
        for index in range(len(array) - 1 - pass_num):
            compare += 1
            if array[index] > array[index + 1]:
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
                exchange += 1
    return (compare, exchange)

def insertion_count(array):
    """Insertion sorts array in ascending order,
    counts comparisons and exchanges"""
    compare, exchange = 0, 0
    for index in range(1, len(array)):
        value = array[index]
        pos = index - 1
        compare += 1
        while pos >= 0 and array[pos] > value:
            array[pos + 1] = array[pos]
            pos -= 1
            exchange += 1
            if pos >= 0:
                compare += 1
        array[pos + 1] = value
    return (compare, exchange)
