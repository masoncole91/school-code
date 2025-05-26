def amount(A, S):
    """from input array, return list:
    -of unique combos summing target value;
    -else, empty;
    don't repeat combos or pass a value's input frequency;
    time complexity O(len(A)^S)"""
    result = []

    # track frequencies to avoid repeats
    count = {num:0 for num in A}
    for num in A:
        count[num] += 1

    # remove repeats, as count dict tracks instances;
    A = sorted(set(A))

    amount_helper(A, 0, result, S, [], count)
    return result

def amount_helper(nums, start, result, remains, combo, count):
    """amount() helper function;
    recurse and find unique combos without passing a value's frequency;
    code repurposed from:
    Exploration 5.2: Backtracking - Combination Sum Problem"""

    # if sum reached, log combo
    if remains == 0:
        result.append(combo[:])
        return
    elif remains < 0:
        return

    for indice in range(start, len(nums)):

        # add and recurse, checking validity
        if count[nums[indice]] > 0 and nums[indice] <= remains:
            combo.append(nums[indice])
            count[nums[indice]] -= 1
            amount_helper(nums, indice, result, remains - nums[indice], combo, count)

            # let new combos use the value
            count[nums[indice]] += 1

            # try next value
            combo.pop()
