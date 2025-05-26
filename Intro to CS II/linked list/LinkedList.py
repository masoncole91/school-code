"""
Author: Mason Blanford
GitHub: GitHub.com/MasonCB
Date: Nov. 9, 2022
Description: Recursively manages linked list
"""

# pylint: disable = invalid-name

class Node:                         # pylint: disable = too-few-public-methods
    """Represents a linked list node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    """Initializes, manages a linked list"""
    def __init__(self):
        self._head = None

    def add(self, val):
        """Adds node with val to linked list"""
        return self.rec_add(val)

    def contains(self, key):
        """Returns True if list has node with specific value,
        False if not"""
        self.rec_contains(key)
        current = self._head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def get_head(self):
        """Returns head of linked list node"""
        return self._head

    def insert(self, val, pos):
        """Puts node with val into linked list at certain position"""
        self.rec_insert(val, pos)

    def remove(self, val):
        """Removes node with val from linked list"""
        self.rec_remove(val, current=None)

    def reverse(self):
        """Reverses linked list"""
        return self.rec_reverse()

    def to_plain_list(self):
        """Returns regular (non-linked) list with same values"""
        return self.rec_to_plain_list([])

    # Helper functions #############################

    def rec_add(self, val, current=None):
        """Helper function for add()
        with default current argument"""
        if self._head is None:
            self._head = Node(val)
            return
        if current is None:
            current = self._head
        if current.next is not None:
            return self.rec_add(val, current=current.next)
        current.next = Node(val)

    def rec_contains(self, key, current=None):
        """Helper function for contains()"""
        if current is not None and current.next is None:
            return False
        if self._head is None:
            return False
        if current is None:
            current = self._head
        if current is not None:
            if current.data == key:
                return True
            return self.rec_contains(key, current=current.next)
        return False

    def rec_insert(self, val, pos, current=None, count=0):
        """Puts node with val into linked list at given position"""
        if current is not None and current.next is None:
            self.add(val)
            return

        if self._head is None:
            self.add(val)
            return
        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head.next = temp
            return
        if current is None:
            current = self._head
        if count < pos - 1:
            return self.rec_insert(val, pos, current=current.next, count=count+1)

        if current.next is not None:
            temp = current.next
            current.next = Node(val)
            current.next.next = temp

    def rec_remove(self, val, prev = None, current=None):
        """Helper function for remove()"""
        if current is not None and val == current:
            if current.next is not None:
                prev.next = current.next
                return
        if self._head is None:      # if list is empty
            return
        if self._head.data == val:  # if need to remove head
            self._head = self._head.next
            return
        if current is None:
            current = self._head
        if current.data != val:
            return self.rec_remove(val, prev=current, current=current.next)
        if current is not None:
            prev.next = current.next

    def rec_reverse(self, prev=None, current=None):
        """Helper function for reverse function"""
        if current is None and prev is not None:
            self._head = prev
            return

        if current is not None:
            self._head = prev

        if current is None:
            current = self._head

        following = current.next
        current.next = prev
        self.rec_reverse(prev=current, current=following)

    def rec_to_plain_list(self, result, current=None):
        """Helper function for to_plain_list()
        with saved array, default arg current"""
        if current is not None and current.next is None:
            result += [current.data]
            return result

        if current is None:
            current = self._head

        result += [current.data]
        current = current.next

        if current is not None:
            return self.rec_to_plain_list(result, current)

        return result
