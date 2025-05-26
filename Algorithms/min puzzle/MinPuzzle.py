from heapq import heappop, heappush


def minEffort(puzzle):  # noqa
    """
    find, return lowest cost to travel 2D matrix;
    O((m*n)log(m*n)) runtime, with m, n as input dimensions

    code used from Oregon State (CS 325):
    - Exploration 7.3: Dijkstra's algorithm

    :param puzzle: 2D matrix
    :type puzzle: list
    """

    # get all rows, columns as boundaries
    # O(1) runtime
    rows, cols = len(puzzle), len(puzzle[0])

    # make minheap with current cost, row, column
    # log best choice each loop
    # O(1) runtime
    cost, row, col = 0, 0, 0
    heap = [(cost, row, col)]

    # log visited cells to stop duplicates
    # O(rows * cols) runtime
    cache = [[False] * cols for _ in range(rows)]

    # log cost so far
    # O(1) runtime
    max_cost = 0

    # loop until heap empty
    # O(rows * cols) max runtime
    while heap:

        # pop lowest-cost node from heap
        # O(log(rows * cols)) runtime
        cost, row, col = heappop(heap)

        # mark node visited; log new cost
        # O(1) runtime
        cache[row][col] = True
        max_cost = max(max_cost, cost)

        # return solution if last node reached
        if row == (rows - 1) and col == (cols - 1):
            return max_cost

        # find orthogonal neighbors from coordinates
        # O(1) runtime — i.e., four loops always
        for new_row, new_col in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            choice_row, choice_col = row + new_row, col + new_col

            # ensure neighbor in-bounds
            # O(1) runtime
            if (0 <= choice_row < rows) and (0 <= choice_col < cols) and not cache[choice_row][choice_col]:
                new_cost = abs(puzzle[choice_row][choice_col] - puzzle[row][col])

                # push new cost to heap
                # O(log(rows * cols))
                heappush(heap, (new_cost, choice_row, choice_col))

    # return cost if last node not reached
    return max_cost

