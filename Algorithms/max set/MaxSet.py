def max_independent_set(nums):
    """find the non-consecutive items in array,
    composing the max possible sum;
    uses code partly from knapsack pseudocode in:
    Exploration 4.2: Dynamic Programming - 0-1 Knapsack Problem;
    Exploration 4.3: Dynamic Programming - Find Optimal Solutions"""

    # init memo array for bottom-up tabulation;
    # subproblems are the max sums so far in nums
    cache = [0] * len(nums)

    # base case: empty nums
    if len(nums) == 0:
        return []

    # first indice's max sum is first item;
    # second max sum is first or second item, since non-consecutive;
    cache[0] = nums[0]
    cache[1] = max(nums[1], nums[0])

    # Exploration 4.2: Dynamic Programming - 0-1 Knapsack Problem
    for indice in range(2, len(nums)):

        # recurrence relation
        cache[indice] = max(cache[indice - 1], nums[indice] + cache[indice - 2])

        # edge case of zero last item,
        # succeeding all negative values
        if nums[indice] > cache[indice]:
            cache[indice] = nums[indice]

    # if zero and all negative values,
    # avoid iterating again
    if cache[len(cache) - 1] == 0:
        return [0]

    # backtrack:
    # if memo item changes,
    # input item is in non-consequtive subsequence;
    # Exploration 4.3: Dynamic Programming - Find Optimal Solutions
    subseq = []
    indice = len(cache) - 1
    while indice > -1:
        if nums[indice] > 0 and cache[indice] != cache[indice - 1]:
            subseq.append(nums[indice])
            indice -= 2
        else:
            indice -= 1

    if len(subseq) == 0:
        subseq = [cache[len(cache) - 1]]

    return subseq[::-1]