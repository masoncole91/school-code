"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Oct. 18, 2022
Description: Sorts array of strings in alphabetical order, ignoring case
"""

def string_sort(array):
    """Alphabetizes list by insertion sort, ignoring case"""
    for index in range(1, len(array)):
        val = array[index]
        pos = index - 1
        while pos >= 0 and array[pos].lower() > val.lower():
            array[pos + 1] = array[pos]
            pos -= 1
        array[pos + 1] = val
