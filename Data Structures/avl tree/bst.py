# Name: Mason Blanford
# OSU Email: blanform@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4 (BST/AVL Trees)
# Due Date: Monday, Feb. 27
# Description: binary search tree

import random
from queue_and_stack import Queue, Stack

class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)

class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """add tree node:
        - left subtree if less;
        - right subtree if equal or more;
        O(n) runtime"""

        # init node
        node = BSTNode(value)

        # start if empty
        if not self._root:
            self._root = node
            return

        # traverse tree with swap
        # left if less, right or more
        # add if empty
        swap = self._root
        while swap:
            if value < swap.value:
                if swap.left:
                    swap = swap.left
                else:
                    swap.left = node
                    break
            else:
                if swap.right:
                    swap = swap.right
                else:
                    swap.right = node
                    break

    # rewrite without recursion, worried about complexity on two subtree cases particularly
    def remove(self, value: object) -> bool:
        """delete node, return:
        - True if removed;
        - else False;
        if two subtrees, replace with right subtree's left child;
        if one, replace with subtree;
        O(n) runtime"""

        # return False if empty
        if not self._root:
            return False

        swap = self._root
        parent, target = None, None

        # find parent, target
        # similar to add() iteration
        while swap:

            # if break, parent is target parent
            parent = swap

            if value < swap.value:
                if swap.left and swap.left.value == value:
                    target = swap.left
                    break
                swap = swap.left
            elif value > swap.value:
                if swap.right and swap.right.value == value:
                    target = swap.right
                    break
                swap = swap.right

            # break if swap equals target
            else:
                break

        # if target is root
        # could say "if parent == target" but why chance it
        if self._root.value == value:
            target = self._root

        # exit if value not in tree
        elif not target:
            return False

        # identify case, remove target, instill successor
        if target.left and target.right:
            return self._remove_two_subtrees(parent, target)
        elif target.left or target.right:
            return self._remove_one_subtree(parent, target)
        else:
            return self._remove_no_subtrees(parent, target)

    def _remove_no_subtrees(self, parent: BSTNode, target: BSTNode) -> None:
        """remove() helper function;
        remove target node if no subtrees"""

        # root is target
        if self._root == target:
            self._root = None
            return True

        # left subtree
        if parent.left and parent.left == target:
            parent.left = None
            return True

        # right subtree
        parent.right = None
        return True

    def _remove_one_subtree(self, parent: BSTNode, target: BSTNode) -> None:
        """remove() helper function;
        remove target node if one subtree;
        replace with subtree"""

        # root is target
        if self._root == target:
            self._root = self._root.left if self._root.left else self._root.right
            return True

        # left subtree
        if parent.left and parent.left == target:
            parent.left = target.left if target.left else target.right
            return True

        # right subtree
        parent.right = target.right if target.right else target.left
        return True

    def _remove_two_subtrees(self, parent: BSTNode, target: BSTNode) -> None:
        """remove() helper function;
        remove target node if two subtrees;
        replace with in-order successor (i.e., right subtree min value)"""

        # find right subtree min value
        new_parent, new_target = target, target.right
        while new_target.left:
            new_parent = new_target
            new_target = new_target.left

        # instill successor
        target.value = new_target.value

        # remove successor case
        if new_target.left and new_target.right:
            return self._remove_two_subtrees(new_parent, new_target)
        elif new_target.left or new_target.right:
            return self._remove_one_subtree(new_parent, new_target)
        else:
            return self._remove_no_subtrees(new_parent, new_target)

    def contains(self, value: object, swap=None) -> bool:
        """return True if value in tree, else False;
        O(n) runtime"""

        # avoid recursion if possible
        if not self._root:
            return False
        if self._root.value == value:
            return True

        # recurse only once if possible
        if not swap:
            return self.contains(value, self._root)
        if swap.value == value:
            return True

        # recurse until value found
        if swap.left and value < swap.value:
            return self.contains(value, swap.left)
        if swap.right and value >= swap.value:
            return self.contains(value, swap.right)

        # False if not found
        return False

    def inorder_traversal(self, node=None, queue=None) -> Queue:
        """traverse tree in-order;
        return Queue empty or with nodes;
        O(n) runtime"""

        # return empty if no tree
        if not self._root:
            queue = Queue()
            return queue

        # start traversal
        if not node:
            queue = Queue()
            return self.inorder_traversal(self._root, queue)

        # find minimum to enqueue
        if node.left:
            self.inorder_traversal(node.left, queue)

        queue.enqueue(node.value)

        # recurse for right subtree;
        # check next minimum before enqueueing
        if node.right:
            self.inorder_traversal(node.right, queue)

        return queue

    def find_min(self, swap=None) -> object:
        """find minimum value;
        return None if empty;
        O(n) runtime"""

        # stop if empty
        if self.is_empty():
            return None

        # recurse only once if possible
        if not swap:
            return self.find_min(self._root)

        # recurse until min
        if swap.left:
            return self.find_min(swap.left)

        return swap.value

    def find_max(self, swap=None) -> object:
        """return maximum value;
        return None if empty;
        O(n)"""

        # stop if empty
        if self.is_empty():
            return None

        # recurse only once if possible
        if not swap:
            return self.find_max(self._root)

        # recurse until max
        if swap.right:
            return self.find_max(swap.right)

        return swap.value

    def is_empty(self) -> bool:
        """return True if empty; else False;
        O(1) runtime"""
        return False if self._root else True

    def make_empty(self) -> None:
        """remove all nodes;
        O(1) runtime"""
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
