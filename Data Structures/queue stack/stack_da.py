# Name: Mason Blanford
# OSU Email: blanform@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 (DynamicArray Stack)
# Due Date: Feb. 13, 2023
# Description: stack abstract data type (ADT);
#               linear storage in Last-In-First-Out (LIFO) or First-In-Last-Out (FILO);
#               items removed only from end they were added

from dynamic_array import *

class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass

class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """add item to stack top;
         O(1) amortized runtime;
         (i.e., complexity rarely higher than O(1))"""
        self._da.append(value)

    def pop(self) -> object:
        """remove top stack item, return value;
        raise StackException if empty;
        O(1) amortized runtime;
        (i.e., complexity rarely higher than O(1))"""
        if self._da.is_empty():
            raise StackException

        val = self._da[self.size() - 1]
        self._da.remove_at_index(self.size() - 1)
        return val

    def top(self) -> object:
        """return top stack item without removal;
        O(1) runtime"""
        if self._da.is_empty():
            raise StackException
        return self._da[self.size() - 1]

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
