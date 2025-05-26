# Name: Mason Blanford
# OSU Email: blanform@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6 (hash maps)
# Due Date: Friday, March 17
# Description: separate chaining hash map with dynamic array, linked lists

from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)

class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        add or update key-value pair;
        double capacity when load factor greater or equal to 1.0
        """

        # double capacity when high load factor
        # assess load factor with put(), not resize_table()
        if self.table_load() >= 1.0:
            self.resize_table(self._capacity * 2)

        # find hash map indice
        hash_indice = self._hash_function(key) % self._capacity

        # add or update key, value
        node = self._buckets[hash_indice].contains(key)
        if node:
            if node.key == key:
                node.value = value
        else:
            self._buckets[hash_indice].insert(key, value)
            self._size += 1

    def empty_buckets(self) -> int:
        """count empty buckets, return integer"""

        count = self._capacity
        for indice in range(self._capacity):
            pair = self._buckets.get_at_index(indice)

            # if pair, decrement count
            if pair.length() > 0:
                count -= 1

        return count

    def table_load(self) -> float:
        """return load factor"""
        return self._size / self._capacity

    def clear(self) -> None:
        """clear hash map, keep capacity"""

        # O(n) hash clear, O(1) attempts aren't working
        for indice in range(self._capacity):
            self._buckets.set_at_index(indice, LinkedList())

        self._size = 0

    def resize_table(self, new_capacity: int) -> None:
        """
        change internal capacity, keep key-value pairs;
        return if input less than 1;
        check if input prime, make prime if not
        """
        if new_capacity < 1:
            return

        # set capacity to next prime
        # assess load factor with put(), not resize_table()
        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)

        # store old conditions
        old_buckets, old_capacity = self._buckets, self._capacity

        # prep new array
        self._buckets = DynamicArray()
        self._capacity = new_capacity
        self._size = 0

        # prep separate chaining
        for _ in range(new_capacity):
            self._buckets.append(LinkedList())

        # set new hash with put()
        for key in range(old_capacity):
            pair = old_buckets.get_at_index(key)
            for node in pair:
                self.put(node.key, node.value)

    def get(self, key: str):
        """return value if key, else None"""

        hash_indice = self._hash_function(key) % self._capacity
        if self._buckets[hash_indice].contains(key):
            return self._buckets[hash_indice].contains(key).value

    def contains_key(self, key: str) -> bool:
        """return True if key, else False"""

        hash_indice = self._hash_function(key) % self._capacity
        if self._buckets[hash_indice].contains(key):
            return True

        return False

    def remove(self, key: str) -> None:
        """remove key, value else None"""
        if not self.contains_key(key):
            return

        hash_indice = self._hash_function(key) % self._capacity
        self._buckets[hash_indice].remove(key)
        self._size -= 1

    def get_keys_and_values(self) -> DynamicArray:
        """return dynamic array of key-value tuples"""

        array = DynamicArray()
        for indice in range(self._capacity):
            pair = self._buckets.get_at_index(indice)

            # O(n): iteration less than capacity
            for node in pair:
                array.append((node.key, node.value))

        return array

def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    return mode(s), frequency in unsorted array;
    O(n) runtime
    """

    map = HashMap(0, hash_function_1)
    array, freq = DynamicArray(), 0

    # loop to add, update with put() O(1)
    # key is array item, value is frequency
    for indice in range(da.length()):
        val = map.get(da[indice])
        if val:
            map.put(da[indice], val + 1)
        else:
            map.put(da[indice], 1)

    # assess frequency
    # originally in above loop, being cautious on complexity
    for indice in range(da.length()):
        val = map.get(da[indice])
        if val > freq:
            freq = val

    # traverse get_keys_values()
    # should be O(n) if iterations < capacity
    pairs = map.get_keys_and_values()
    for indice in range(pairs.length()):
        if pairs[indice][1] == freq:
            array.append(pairs[indice][0])

    return (array, freq)

# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(23, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")

