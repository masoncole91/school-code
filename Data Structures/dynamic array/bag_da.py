# Name: Mason Blanford
# OSU Email: blanform@oregonstate.edu
# Course: CS261 (Data Structures)
# Assignment: 2
# Due Date: Feb. 6, 2023
# Description: Bag abstract data type (unordered collection of elements)

from dynamic_array import *

class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """add new item to bag at O(1) amortized complexity"""
        # O(n) complexity when capacity reached for resizing array;
        # O(1) otherwise
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """remove item if matching value in O(n) complexity;
         return:
         - True if item removed;
         - False otherwise"""
        for indice in range(self._da.length()):
            if self._da.get_at_index(indice) == value:
                self._da.remove_at_index(indice)
                return True
        return False

    def count(self, value: object) -> int:
        """return number of Bag items that match value;
         O(n) complexity"""
        count = 0
        for indice in range(self._da.length()):
            if self._da.get_at_index(indice) == value:
                count += 1
        return count

    def clear(self) -> None:
        """clear Bag DynamicArray at O(1) complexity"""
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """compare Bag contents with second Bag parameter;
        return:
        - True if Bag arrays have same elements, same frequencies (unordered);
        - else False;
        O(n^2) complexity; no additional data structures or sorting"""
        # don't run if different frequencies
        if self._da.length() != second_bag.size():
            return False

        count_all = 0
        for indice in range(self._da.length()):

            # avoid long conditional below
            count1 = self.count(self._da.get_at_index(indice))
            count2 = second_bag.count(self._da.get_at_index(indice))

            # if count(1) is count(2):
            # - second_bag loop for item check is unnecessary nested loop;
            # Bag lengths already compared above, also
            if count1 == count2:
                count_all += 1

        return True if count_all == self._da.length() else False

    def __iter__(self):
        """initializes index for Bag iteration"""
        self._index = 0
        return self

    def __next__(self):
        """return next Bag item for iteration"""
        try:
            value = self._da.get_at_index(self._index)
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
