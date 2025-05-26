# Name: Mason Blanford
# OSU Email: blanform@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4 (BST/AVL Trees)
# Due Date: Monday, Feb. 27
# Description: AVL tree

import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST

class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """
    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False
                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)

        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """add node and rebalance;
        each node with balance -1, 0, or 1;
        if duplicate, change nothing;
        O(log N) runtime"""

        # init node
        node = AVLNode(value)
        if not self._root:
            self._root = node
            return self._root

        # iterate, add as like BST
        swap = self._root
        while swap:
            if value < swap.value:
                if swap.left:
                    swap = swap.left
                else:
                    swap.left = node
                    break
            elif value > swap.value:
                if swap.right:
                    swap = swap.right
                else:
                    swap.right = node
                    break
            else:
                break

        # set node parent
        node.parent = swap

        # node height update first, so parent updates accordingly
        self._update_height(node)
        self._update_height(node.parent)

        # while loop to traverse up tree and rebalance
        parent = node.parent
        while parent:
            self._rebalance(parent)
            parent = parent.parent

    # ran out of time on remove() i'm afraid, it's been a challenging few days
    def remove(self, value: object) -> bool:
        """remove node;
        return:
        - True if removed;
        - else False;
        O(log N) runtime"""

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
            self._remove_two_subtrees(parent, target)
        elif target.left or target.right:
            self._remove_one_subtree(parent, target)
        else:
            self._remove_no_subtrees(parent, target)

        while parent:
            self._rebalance(parent)
            parent = parent.parent

        if not self.is_valid_avl():
            print("NOT VALID WHY...................................................................................")

        return True

    def _rebalance(self, node: AVLNode) -> None:
        """add() help method;
        update height, check balance;
        if unbalanced, rebalance tree;
        O(log N) runtime"""

        # update node in add() while loop
        # calculate balance
        self._update_height(node)
        balance = self._get_balance_factor(node)

        # right-right, right-left cases
        if balance < -1:
            if self._get_balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)

        # left-left, left-right cases
        if balance > 1:
            if self._get_balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """_rebalance() help method;
        balance subtree by rotating counter-clockwise;
        assign:
        1) right subtree as new parent;
        2) input node as new left subtree;
        3) new parent's left subtree as new right subtree;
        O(1) runtime"""

        # new root is old root right subtree
        new_root = node.right

        # store new left subtree's current left subtree
        # otherwise, wrong pointers lead to invalid msg
        swap = new_root.left

        # old root right subtree now in right place
        node.right = swap

        # set new parent for new left subtree's current left subtree
        # this bug took me hours
        if swap:
            swap.parent = node

        # set new root left subtree
        new_root.left = node

        # set parent pointers
        if node.parent:
            if node.parent.left == node:
                node.parent.left = new_root
            else:
                node.parent.right = new_root
        else:
            self._root = new_root

        # set new, old root parent pointers
        new_root.parent = node.parent
        node.parent = new_root

        # update height
        self._update_height(node)
        self._update_height(new_root)

        # return root for left-right case
        return new_root

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """_rebalance() help method;
        balance subtree by rotating clockwise;
        assign:
        1) left subtree as new parent;
        2) input node as new right subtree;
        3) new parent's right subtree as new left subtree;
        O(1) runtime"""

        # new root is old root left subtree
        new_root = node.left

        # store new left subtree's current left subtree
        # otherwise, wrong pointers lead to invalid msg
        swap = new_root.right

        # old root right subtree now in right place
        node.left = swap

        # set new parent for new left subtree's current left subtree
        if swap:
            swap.parent = node

        # set new root left subtree
        new_root.right = node

        # set parent pointers
        if node.parent:
            if node.parent.right == node:
                node.parent.right = new_root
            else:
                node.parent.left = new_root
        else:
            self._root = new_root

        # set new, old root parent pointers
        new_root.parent = node.parent
        node.parent = new_root

        # update height
        self._update_height(node)
        self._update_height(new_root)

        return new_root

    def _update_height(self, node: AVLNode) -> None:
        """add() help method;
        check height of input node (i.e., max subtree height plus 1);
        O(1) runtime"""
        left_subtree_height = self._get_height(node.left)
        right_subtree_height = self._get_height(node.right)
        node.height = 1 + max(left_subtree_height, right_subtree_height)

    def _get_height(self, node: AVLNode) -> int:
        """_update_height() help method;
        return height of input node:
        - if no node, -1;
        - else node height"""
        if not node:
            return -1
        return node.height

    def _get_balance_factor(self, node: AVLNode) -> int:
        """_rebalance() help method;
        return balance of input node"""
        left_subtree_height = self._get_height(node.left)
        right_subtree_height = self._get_height(node.right)
        return left_subtree_height - right_subtree_height

    def _remove_no_subtrees(self, parent: AVLNode, target: AVLNode) -> None:
        """remove() helper function;
        remove target node if no subtrees"""

        # root is target
        if self._root == target:
            self._root = None

        # left subtree
        if parent.left and parent.left == target:
            parent.left = None

        # right subtree
        else:
            parent.right = None

    def _remove_one_subtree(self, parent: AVLNode, target: AVLNode) -> None:
        """remove() helper function;
        remove target node if one subtree;
        replace with subtree"""

        # root is target
        if self._root == target:
            self._root = self._root.left if self._root.left else self._root.right

        # left subtree
        if parent.left and parent.left == target:
            parent.left = target.left if target.left else target.right

        # right subtree
        parent.right = target.right if target.right else target.left

    def _remove_two_subtrees(self, parent: BSTNode, target: BSTNode) -> None:
        """remove() helper function;
        remove target node if two subtrees;
        replace with in-order successor (i.e., right subtree min value)"""

        # find right subtree min value
        new_parent, new_target = target, target.right
        while new_target.left:
            new_parent = new_target
            new_target = new_target.left

        # remove target, instill successor
        target.value = new_target.value

        # remove successor case
        if new_target.left and new_target.right:
            return self._remove_two_subtrees(new_parent, new_target)
        elif new_target.left or new_target.right:
            return self._remove_one_subtree(new_parent, new_target)
        else:
            return self._remove_no_subtrees(new_parent, new_target)

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)

    # print("\nPDF - method remove() example 5")
    # print("-------------------------------")
    # for _ in range(100):
    #     case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #     tree = AVL(case)
    #     for value in case[::2]:
    #         tree.remove(value)
    #     if not tree.is_valid_avl():
    #         raise Exception("PROBLEM WITH REMOVE OPERATION")
    # print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
