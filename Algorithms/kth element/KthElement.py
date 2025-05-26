# Name: Mason Blanford
# Date: 4-17-23
# CS 325 (Algorithms Analysis)
# Homework 2, Problem 3b

def kthElement(array1, array2, pos):
    """merge two arrays with merge_sort() helper
    return element at pos indice"""
    pos -= 1
    array = array1 + array2
    merge_sort(array, 0, len(array) - 1)
    return array[pos]

def merge_sort(array, start, end):
    """sort array with merge-sort algorithm
    taken from:
    - Oregon State University, CS 325
    - Exploration 2.3.1: Divide-and-Conquer Algorithms"""
    if(start < end):
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        merge(array, start, mid, end)

def merge(array, start, mid, end):
    """merge two sorted subarrays
    taken from:
    - Oregon State University, CS 325
    - Exploration 2.3.1: Divide-and-Conquer Algorithms"""
    # generate temp arrays
    left_array_size, right_array_size = (mid - start) + 1, (end - mid)
    left_array, right_array = [0] * left_array_size, [0] * right_array_size

    # store input arrays in temp arrays
    for indice in range(0, left_array_size):
        left_array[indice] = array[start + indice]
    for indice in range(0, right_array_size):
        right_array[indice] = array[mid + 1 + indice]

    # merge two temp arrays into one array
    left_indice, right_indice = 0, 0
    pos = start
    while (left_indice < left_array_size and right_indice < right_array_size):
        if (left_array[left_indice] < right_array[right_indice]):
            array[pos] = left_array[left_indice]
            left_indice += 1
        else:
            array[pos] = right_array[right_indice]
            right_indice += 1
        pos += 1

    # copy remaining elements of both arrays
    while (left_indice < left_array_size):
        array[pos] = left_array[left_indice]
        pos += 1
        left_indice += 1
    while (right_indice < right_array_size):
        array[pos] = right_array[right_indice]
        pos += 1
        right_indice += 1
