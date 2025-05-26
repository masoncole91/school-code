"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Nov. 2, 2022
Description: Determines if array has only decreasing numbers
"""

def is_decreasing(array):
    """Returns True if numbers are strictly decreasing"""
    pos = 0
    if len(array) == 1:
        return True
    if len(array) == 2 and pos != 0:
        return True
    if array[0] <= array[1]:
        return False
    pos += 1
    print(array)
    return is_decreasing(array[pos:])
