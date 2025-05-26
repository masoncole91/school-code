"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Nov. 2, 2022
Description: Recursively determines max of array
"""

def list_max(array):
    """Returns highest integer or float in array"""
    pos = 0
    if len(array) == 1:
        return array[0]
    if array[0] > array[1]:
        del array[1]
    elif array[0] < array[1] or array[0] == array[1]:
        del array[0]
    pos += 1
    return list_max(array)
