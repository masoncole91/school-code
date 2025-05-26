from heapq import heappush


def Prims(G): # noqa
    """
    find minimum spanning tree for undirected graph;

    code used from Oregon State University's CS 325:
        Exploration 8.1: Minimum Spanning Tree - Prim's Algorithm;

    :param G: undirected graph as 2D matrix
    :type G: list
    :rtype: list of tuples with integers
    :return: [(vertex1, vertex2, weight), ...]
    """
    start, end, cost = 0, None, float("infinity")
    visited = {start}

    mst = []
    while len(visited) < len(G):
        for vertex1 in visited:
            for vertex2 in range(len(G)):
                if vertex2 not in visited and 0 < G[vertex2][vertex1] < cost:
                    start, end, cost = vertex1, vertex2, G[vertex2][vertex1]

        visited.add(end)
        heappush(mst, (start, end, cost))
        cost = float("infinity")

    return mst

