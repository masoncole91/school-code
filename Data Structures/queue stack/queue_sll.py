# Name: Mason Blanford
# OSU Email: blanform@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 (LinkedList Queue)
# Due Date: Feb. 13, 2023
# Description: queue abstract data type (ADT);
#               by singly linked list storage (i.e., non-linear nodes)

from SLNode import SLNode

class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass

class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """add value to end of queue;
        O(1) runtime"""
        new = SLNode(value)

        # assign if empty;
        # tail must point to head;
        # else tail node has no next for appending values
        if self.is_empty():
            self._head = new
            self._tail = self._head

        # no head pointer, since appending
        else:
            self._tail.next = new
            self._tail = new

    def dequeue(self) -> object:
        """remove, return first queue item;
        raise QueueException if empty;
        O(1) runtime"""
        if self.is_empty():
            raise QueueException

        # assign first node value;
        # skip over
        val = self._head.value
        self._head = self._head.next
        return val

    def front(self) -> object:
        """return front queue item;
        raise QueueException if empty;
        O(1) runtime"""
        if self.is_empty():
            raise QueueException
        return self._head.value

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
