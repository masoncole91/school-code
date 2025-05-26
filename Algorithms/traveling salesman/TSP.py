def solve_tsp(G):   # noqa
    """
    approximate the Traveling Salesman Problem (TSP);
    use the nearest-neighbor heuristic

    find a Hamiltonian cycle;
    i.e., visit all nodes at least cost, return to start

    :param G: graph (complete, undirected, weighted)
    :type G: nested list, 2D matrix
    :return: Hamiltonian cycle
    :rtype: list

    TSP info from Oregon State University's CS 325:
    - Exploration 9.3: Approximation Algorithms to Solve NP-Hard Problems

    Dev Genius blog helped with nearest-neighbor code:
    - https://blog.devgenius.io/traveling-salesman-problem-nearest-neighbor-algorithm-solution
    """
    # init first node, final list; log nodes visited
    start = 0
    tour, memo = [start], set()

    # nested loop O(V^2), V all vertices;
    # outer loop O(V)
    while len(tour) < len(G):

        # log node, prepare greedy
        memo.add(start)
        neighbor, min_weight = None, float("infinity")

        # O(V)
        for vertex in range(len(G)):

            # mull greedy choice;
            # maybe greed good... maybe not
            if vertex not in memo:
                weight = G[start][vertex]

                # keep lowest cost if not zero, i.e., incomplete
                if 0 < weight < min_weight:
                    neighbor = vertex
                    min_weight = weight

        # commit greed
        start = neighbor
        tour.append(start)

    # return to root
    tour.append(0)
    return tour
