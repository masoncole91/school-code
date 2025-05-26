# Name: Mason Blanford
# OSU Email: blanform@oregonstate.edu
# Course: Data Structures (CS 261)
# Assignment 1: Python Fundamentals Review
# Due Date: Jan. 30
# Description: Algorithms written by time complexity.
# All are intended as O(n), except for count_sort, which is O(n+1)

import random
import static_array
from static_array import *

# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------
def min_max(arr: StaticArray) -> (int, int):
    """Returns tuple with minimum, maximum values of input array"""
    # set min, max defaults
    min, max = arr.get(0), arr.get(0)

    for indice in range(arr.length()):
        # evaluate new min, max each indice
        if arr.get(indice) < min:
            min = arr.get(indice)
        if arr.get(indice) > max:
            max = arr.get(indice)

    return min, max

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------
def fizz_buzz(arr: StaticArray) -> StaticArray:
    """Returns new StaticArray object that prints:
    "fizz" if integer divisible by 3;
    "buzz" if divisible by 5;
    and "fizzbuzz" if divisible by 3 and 5"""
    new = StaticArray(arr.length())

    for indice in range(arr.length()):
        # exclude mutual condition first
        if arr.get(indice) % 3 == 0 \
                and arr.get(indice) % 5 == 0:
            new.set(indice, "fizzbuzz")

        # avoid inclusive array change with elif
        elif arr.get(indice) % 3 == 0:
            new.set(indice, "fizz")
        elif arr.get(indice) % 5 == 0:
            new.set(indice, "buzz")

        # fill rest of array
        else:
            new.set(indice, arr[indice])

    return new

# ------------------- PROBLEM 3 - REVERSE -----------------------------------
def reverse(arr: StaticArray) -> None:
    """Reverses existing StaticArray object"""
    start, stop = 0, arr.length() - 1

    for indice in range(start, stop):
        # assign swap variable for no duplicates
        swap = arr.get(start)

        # prevent further reversal after finish
        # assignments start at both ends, meet in middle
        if start < arr.length() // 2:
            arr.set(start, arr.get(stop))
            arr.set(stop, swap)
            start += 1
            stop -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """Receives StaticArray, integer value "steps";
    Returns new StaticArray rotated by value"""
    new = StaticArray(arr.length())

    # loop back to beginning of array
    start = steps % arr.length()

    for indice in range(new.length()):
        new.set(start, arr.get(indice))

        # positive steps value loops right
        # negative steps value automatically loops left
        start = (start + 1) % new.length()

    return new

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """Returns StaticArray of consecutive integers between two inputs"""
    # find array length necessary
    steps = abs(start - end) + 1
    new = StaticArray(steps)

    for indice in range(steps):
        new.set(indice, start)

        # move right if positive, left if negative
        start = start + 1 if start < end else start - 1

    return new

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """Returns 1 if StaticArray sorted by ascending;
    -1 if descending order; otherwise 0"""
    result1, result2 = None, None

    # loop to determine changes in elements
    for indice in range(arr.length() - 1):
        if arr.get(indice) < arr.get(indice + 1):
            result1 = 1
    for indice in range(arr.length() - 1):
        if arr.get(indice) > arr.get(indice + 1):
            result2 = -1
    for indice in range(arr.length() - 1):
        if arr.get(indice) == arr.get(indice + 1):
            return 0

    # return final conditions
    if result1 and result2:
        return 0
    if result1 or (arr.length() == 1):
        return 1
    else:
        return -1

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """Returns array mode with frequency"""
    # store result in tuple
    # avoid another data structure; store only the latest highest count
    mode = (arr.get(0), 1)
    count = 1

    for indice in range(arr.length() - 1):

        # increment count
        if arr.get(indice) == arr.get(indice + 1):
            count += 1
            if count > mode[1]:
                mode = (arr.get(indice), count)

        # reset count if no new repetition
        else:
            count = 1

    return mode

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """Returns new StaticArray with duplicates removed"""
    swap = StaticArray(arr.length())

    # return single-element array if present
    swap.set(0, arr.get(0))

    # determine length of new array
    count = 1
    if arr.length() > 1:
        for indice in range(1, arr.length()):

            # main logic condition
            if arr.get(indice) != (arr.get(indice - 1) or arr.get(indice + 1)):
                swap.set(indice, arr.get(indice))
                count += 1

        new = StaticArray(count)
        pos = 0

        # populate new array
        for indice in range(swap.length()):
            if swap.get(indice):
                new.set(pos, swap.get(indice))
                pos += 1

        return new
    return swap

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """Returns new StaticArray object in non-ascending order through count-sort;
    the algorithm uses two arrays:
    a count array for determining frequency;
    and a sort array for ordering and duplication"""

    # find count array length with min_max helper function
    domain = min_max(arr)
    count = StaticArray(abs(domain[1] - domain[0]) + 1)

    # store frequencies as indices in count array
    # bypasses need for nested loop
    for indice in range(arr.length()):
        slot = arr.get(indice) - domain[0]

        if not count.get(slot):
            count.set(slot, 1)
        else:
            count.set(slot, count.get(slot) + 1)

    # avoid nested loop again:
    # derive input values algebraically from
    # (slot = arr.get(indice) - domain[0])
    sort = StaticArray(arr.length())
    pos = 0

    for indice in range(count.length()):
        arr_indice = indice + domain[0]

        # limit complexity in nested loop with constant value
        if count.get(indice):
            for _ in range(count.get(indice)):
                sort.set(pos, arr_indice)
                pos += 1

    # reverse final array
    reverse(sort)

    return sort

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """Returns new StaticArray with values
    from original array squared in non-descending order"""
    new = StaticArray(arr.length())

    # initialize variables if squares need sorting
    mid = 0
    half1, half2 = 0, 0

    # square values
    # determine if array halved by 0 or change in sign
    for indice in range(arr.length()):
        if arr.get(indice) == 0:
            mid = indice
            half1, half2 = mid - 1, mid + 1
        elif arr.get(indice) < 0 and arr.get(indice + 1) > 0:
            half1, half2 = indice, indice + 1

        new.set(indice, arr.get(indice) ** 2)

    # use is_sorted to determine if sorting squares necessary
    # reverse if necessary
    if is_sorted(new) == 1:
        pass
    elif is_sorted(new) == -1:
        reverse(new)
    else:
        sort = StaticArray(new.length())
        sort.set(0, 0)
        inc = 1

        # start at indices in middle, work outwards with two pointers
        for indice in range(new.length() // 2):
            if new.get(half1) < new.get(half2):
                sort.set(inc, new.get(half1))
                sort.set(inc + 1, new.get(half2))
            elif new.get(half1) > new.get(half2):
                sort.set(inc, new.get(half2))
                sort.set(inc + 1, new.get(half1))
            elif new.get(half1) == new.get(half2):
                sort.set(inc, new.get(half1))
                sort.set(inc + 1, new.get(half2))
            inc += 2
            half1 -= 1
            half2 += 1

        # if squares need sorting
        return sort

    # if no sorting for squares
    return new

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
