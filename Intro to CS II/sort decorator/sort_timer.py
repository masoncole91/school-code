"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Nov. 15, 2022
Description: Compares sorting algorithms, plots results
"""

import time
import random
from functools import wraps
from matplotlib import pyplot

def sort_timer(func):
    """Decorates, times sorting algorithms in seconds"""
    @wraps(func)            # retains decorated function doc info
    def wrapper(*args):
        """Runs before each sort algorithm,
        computes, returns time"""
        start_time = time.perf_counter()
        func(*args)         # function runes after timer starts
        end_time = time.perf_counter()
        return end_time - start_time
    return wrapper

@sort_timer
def bubble_sort(lst):
    """Sorts array in ascending order,
    copied from Module 4 per the ReadMe"""
    for num in range(len(lst) - 1):
        for index in range(len(lst) - 1 - num):
            if lst[index] > lst[index + 1]:
                temp = lst[index]
                lst[index] = lst[index + 1]
                lst[index + 1] = temp

@sort_timer
def insertion_sort(lst):
    """Sorts array in ascending order,
    copied from Module 4 per the ReadMe"""
    for index in range(1, len(lst)):
        value = lst[index]
        pos = index - 1
        while pos >= 0 and lst[pos] > value:
            lst[pos + 1] = lst[pos]
            pos -= 1
        lst[pos + 1] = value

def compare_sorts(func1, func2):
    """Runs bubble, insertion sort algorithms
    for varying array sizes,
    generates plot comparing results"""

    # generate dictionary to store algorithm times
    results = {"bubble_sort": [], "insertion_sort": []}
    trial = 1000
    for _ in range(10):
        array = []
        for _ in range(0, trial):
            array.append(random.randint(1, 10000))
        array_copy1, array_copy2 = array, array
        for (key, val) in results.items():
            if key == "bubble_sort":
                val.append(func1(array_copy1))
            else:
                val.append(func2(array_copy2))
        trial += 1000

    # prepares results for pyplot graph
    elements = list(range(1000, 11000, 1000))
    bubble_vals, insertion_vals = [], []
    for (key, val) in results.items():
        if key == "bubble_sort":
            bubble_vals = val
        else:
            insertion_vals = val

    # graphs results, opens line chart in new window
    pyplot.plot(elements, bubble_vals,
                "ro--", linewidth=2, label="bubble sort")
    pyplot.plot(elements, insertion_vals,
                "go--", linewidth=2, label="insertion sort")
    pyplot.xlabel("number of sorted elements")
    pyplot.ylabel("time (seconds)")
    pyplot.legend(loc="upper left")
    pyplot.show()

# generate results and graph for TA
compare_sorts(bubble_sort, insertion_sort)
