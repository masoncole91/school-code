def powerset_helper(pointer, choices_made, input, result):
    """powerset() helper function;
    recursively break down array,
    generating subsets of each subproblem;
    taken from:
    Exploration 4.4: Backtracking"""

    # log subsets of subproblem
    if pointer > len(input) - 1:
        result.append(choices_made[:])
        return

    # generate subset for new item
    choices_made.append(input[pointer])

    # recursively break down subarray
    powerset_helper(pointer + 1, choices_made, input, result)

    # decrement ongoing array
    choices_made.pop()

    # move to recursively break down next subarray
    powerset_helper(pointer + 1, choices_made, input, result)

def powerset(input):
    """generate powerset of array;
    taken from:
    Exploration 4.4: Backtracking"""

    result = []
    powerset_helper(0, [], input, result)
    return result