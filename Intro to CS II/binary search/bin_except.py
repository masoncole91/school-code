"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Oct. 18, 2022
Description: Modifies binary search algorithm to raise exception if failure
"""

def bin_except(array, target):
    """Searches array for target,
     returns index position in array if found,
     raises TargetNotFound exception if not found"""
    first = 0
    last = len(array) - 1
    while first <= last:
        middle = (first + last) // 2
        if array[middle] == target:
            return middle
        if array[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound

class TargetNotFound(Exception):
    """Custom-defined exception if target not found in array"""
