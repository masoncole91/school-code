import copy


def solve_puzzle(Board, Source, Destination):  # noqa
    """
    return path to cell given a starting point

    :param Board: 2D matrix
    :type Board: list

    :param Source: start cell
    :type Source: tuple

    :param Destination: end cell
    :type Destination: tuple

    :rtype: list of tuples; string
    :return: directions for each cell to visit; direction letters
    """

    # deepcopy board to avoid altering objects
    mimic = copy.deepcopy(Board)
    mimic = _weigh(mimic, Destination)

    # log visited cells to stop duplicates
    cache = set()

    # loop until only barriers or destination
    current, path = Source, [Source]
    while current:

        # pop for current position
        row, col = current[0], current[1]

        # mark visited
        cache.add((row, col))

        # return:
        # - empty if only barriers;
        # - else, destination
        if row == float("infinity") or col == float("infinity"):
            return
        if (row, col) == Destination:
            return path

        # find orthogonal neighbors from coordinates
        min_row, min_col = float("infinity"), float("infinity")
        min_cost = float("infinity")
        for new_row, new_col in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            choice_row, choice_col = row + new_row, col + new_col

            # ensure neighbor in-bounds
            if (0 <= choice_row < len(mimic)) and (0 <= choice_col < len(mimic[0])):
                if (choice_row, choice_col) not in cache:
                    cost = mimic[choice_row][choice_col]

                    # log best choice each loop
                    if cost < min_cost:
                        min_row, min_col = choice_row, choice_col
                        min_cost = cost

        # push new cell to heaps
        current = (min_row, min_col)
        path.append(current)


def _weigh(mimic, Destination):  # noqa
    """assigns eights to each cell"""
    end_row, end_col = Destination
    for row in range(len(mimic)):
        for col in range(len(mimic[0])):
            if mimic[row][col] == "#":
                mimic[row][col] = float("infinity")
            else:
                diff_row = abs(row - end_row)
                diff_col = abs(col - end_col)
                mimic[row][col] = diff_row + diff_col

    return mimic
