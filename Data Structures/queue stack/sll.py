# Name: Mason Blanford
# OSU Email: blanform@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 (LinkedList)
# Due Date: Feb. 13, 2023
# Description: singly linked list abstract data type (ADT);
#               non-contiguous: data nodes link non-linearly by pointers

from SLNode import *

class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass

class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """add new node to linked list start, after front sentinel;
         O(1) runtime"""
        new = SLNode(value)

        # current head value becomes input value
        self._head.value = new.value

        # next becomes current node
        new.next = self._head

        # head becomes initialized node
        self._head = new

    def insert_back(self, value: object) -> None:
        """add node to linked list end;
         O(n) runtime"""
        new = SLNode(value)
        swap = self._head

        # pass over nodes
        while swap.next:
            swap = swap.next

        swap.next = new

    def insert_at_index(self, index: int, value: object) -> None:
        """insert value at linked list indice;
        indice 0 is list's beginning after front sentinel;
        valid indice is [0, N], with N nodes;
        else raise SLLException"""
        if index not in range(0, self.length() + 1):
            raise SLLException

        new = SLNode(value)

        # prepend or append for first or last indice
        if index == 0:
            self.insert_front(new.value)
        elif index == self.length():
            self.insert_back(value)
        else:
            swap = self._head

            # insert_back logic, except for input indice
            for indice in range(self.length()):
                if indice == index:
                    new.next = swap.next
                    swap.next = new
                swap = swap.next

    def remove_at_index(self, index: int) -> None:
        """remove node at linked list indice;
        valid indice is [0, N - 1], with N items;
        else raise SLLException"""
        if index not in range(0, self.length()):
            raise SLLException

        # iterate with swap;
        # else linked list only cuts self._head (i.e., first node)
        if index == 0:
            swap = self._head
            self._head = swap.next

        elif index > 0:
            swap = self._head
            pos = 0
            while pos < index:
                swap = swap.next
                pos += 1

            # assign swap.next node two slots up;
            # after node removed
            swap.next = swap.next.next

    def remove(self, value: object) -> bool:
        """remove first node matching value;
        return:
        - True if node removed;
        - else False"""
        swap = self._head

        while swap.next:
            if swap.next.value == value:
                swap.next = swap.next.next
                return True
            swap = swap.next

        return False

    def count(self, value: object) -> int:
        """count all matching linked list values"""
        swap = self._head
        freq = 0

        while swap.next is not None:
            swap = swap.next
            if swap.value == value:
                freq += 1

        return freq

    def find(self, value: object) -> bool:
        """return:
         - True if value in linked list;
         - else False"""
        swap = self._head

        while swap.next is not None:
            swap = swap.next
            if swap.value == value:
                return True
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """return new linked list of size from start indice;
        valid start_index [0, N - 1], with N items;
        else raise SLLException;
        O(n) runtime"""
        if (start_index < 0 or start_index > self.length() - 1) or size < 0:
            raise SLLException
        if start_index + size > self.length():
            raise SLLException

        new = LinkedList()
        swap = self._head
        pos = 0

        # iterate to start_index
        while pos <= start_index - 1:
            swap = swap.next
            pos += 1

        # append from start_index to size
        while pos < size + start_index:
            swap = swap.next
            new.insert_back(swap.value)
            pos += 1

        return new

if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n")
    lst = LinkedList([0, 1, 2, 3])
    lst.remove_at_index(0)
    print(lst)

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
