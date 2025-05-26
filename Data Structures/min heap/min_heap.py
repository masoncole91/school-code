# Name: Mason Blanford
# OSU Email: blanform@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5 (MinHeap Implementation)
# Due Date: Monday, March 6, 2023
# Description: binary tree min-heap

from dynamic_array import *

class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass

class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """add node, maintain MinHeap property;
         O(log N) runtime"""

        # start heap if empty
        if self.is_empty():
            self._heap.append(node)
            return

        # add before sorting
        self._heap.append(node)

        # maintain O(log N) by only iterating one branch;
        # assign:
        # - indice as current node indice
        # - parent as current parent indice
        indice = self.size() - 1
        parent = (indice - 1) // 2

        # allow for root compare with -1
        while parent > -1:
            if node < self._heap[parent]:
                swap = self._heap[parent]

                # swap nodes
                self._heap[parent] = node
                self._heap[indice] = swap

                # assign indice as current node indice
                indice = parent

            # compare next parent node
            parent = (parent - 1) // 2

    def is_empty(self) -> bool:
        """return:
        - True if heap empty;
        - else, False;
        O(1) runtime"""
        if self._heap.length() == 0:
            return True
        return False

    def get_min(self) -> object:
        """return least node;
        if empty, raise MinHeapException;
        O(1) runtime"""
        if self.is_empty():
            raise MinHeapException
        return self._heap[0]

    def remove_min(self) -> object:
        """remove, return least node;
        replace with left subtree if less;
        if empty, raise MinHeapException;
        O(log N) runtime"""
        if self.is_empty():
            raise MinHeapException

        # return afterward
        removed = self._heap[0]

        # swap min with last node, remove last
        self._heap[0] = self._heap[self.size() - 1]
        self._heap.remove_at_index(self.size() - 1)

        # check if two nodes or less, avoid loop
        if self.size() == 2 and self._heap[0] > self._heap[1]:
            self._heap[1], self._heap[0] = self._heap[0], self._heap[1]
            return removed
        if self.size() == 1:
            return removed

        # maintain MinHeap
        root = 0
        left = (2 * root) + 1
        while left < self.size():
            # find new subtree set
            right = (2 * root) + 2

            # break before DynamicArrayException
            if right >= self.size():
                break

            # left is less than right
            left_less = self._heap[left] and self._heap[left] <= self._heap[right]

            # only left is possible
            only_left = self._heap[left] and not self._heap[right]

            # assign min child
            case = None
            if left_less or only_left:
                case = left
            else:
                case = right

            # prevent case of smaller root assigned lower
            if case and self._heap[root] > self._heap[case]:
                root = self._swap(case, root)

            left = (2 * root) + 1

        return removed

    def _swap(self, child, root):
        """remove_min() helper method;
        swap root, subtree nodes"""
        swap = self._heap[child]
        self._heap[child] = self._heap[root]
        self._heap[root] = swap
        return child

    def build_heap(self, da: DynamicArray) -> None:
        """build MinHeap from random DynamicArray;
        O(n) runtime"""

        # init new heap
        # if heap = da, changes to da affect heap
        # if new DynamicArray(), appending da elements causes O(N log N)
        self._heap = DynamicArray(da)

        # begin with internal nodes, work upward
        # leaf nodes are frivolous comparisons and excluded
        for indice in range((self.size() // 2) - 1, -1, -1):

            root = indice
            left = (2 * indice) + 1
            while left < self.size():
                right = (2 * indice) + 2

                in_bounds = right < self.size()
                left_less = in_bounds and self._heap[left] < self._heap[right]

                # unsure why DynamicArrayException without this redundancy
                if left_less:
                    root = left
                elif in_bounds and not left_less:
                    root = right

                # break if root less
                # avoid unnecessary loop
                if self._heap[indice] <= self._heap[root]:
                    break

                if indice != root:
                    self._heap[indice], self._heap[root] = self._heap[root], self._heap[indice]

                left = (2 * indice) + 1

    def size(self) -> int:
        """return number of nodes;
        O(1) runtime"""
        return self._heap.length()

    def clear(self) -> None:
        """clear heap;
        O(1) runtime"""
        self._heap = DynamicArray()

def heapsort(da: DynamicArray) -> None:
    """sort DynamicArray non-ascending with heapsort algo;
    no new data structures;
    return nothing;
    O(N log N) runtime;
    """

# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    TODO: Write your implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
