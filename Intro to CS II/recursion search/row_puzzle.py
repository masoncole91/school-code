"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Nov.2, 2022
Description: Recursively iterates 1D array for solution
"""

def row_puzzle(array):
    """Returns helper function rec_row_puzzle,
     traverses array with indice as zero, memo as empty list"""
    return rec_row_puzzle(array, 0, [])

def rec_row_puzzle(array, indice, memo):
    """Traverses array, memoizes new indices,
    returns True if solvable, False if not"""
    if indice < 0 or indice > len(array):
        return False
    if indice == len(array) - 1:
        return True

    if indice not in memo:
        memo.append(indice)

    pos = array[indice]
    move_left = indice - pos
    move_right = indice + pos

    if move_right < len(array) and move_right not in memo:
        return rec_row_puzzle(array, move_right, memo)
    if move_left > 0 and move_left not in memo:
        return rec_row_puzzle(array, move_left, memo)

    return False
