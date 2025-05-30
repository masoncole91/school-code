# Name: Mason Blanford
# OSU Email: blanform@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6 (hash maps)
# Due Date: Friday, March 17
# Description: hash map with open address, quadratic probing

from a6_include import (DynamicArray, DynamicArrayException, HashEntry,
                        hash_function_1, hash_function_2)

class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(None)

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
        Increment from given number to find the closest prime number
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
        double capacity when load factor greater or equal to 0.5
        """

        # assess load factor with put(), not resize()
        if self._size / self._capacity >= 0.5:
            self.resize_table(self._capacity * 2)

        # this is ugly code, much refactoring possible, but too much stuff breaks if it's changed
        hash_initial = self._hash_function(key) % self._capacity
        probe = 0
        while True:
            if probe == self._capacity:
                break

            # update if key present
            # tombstone also
            hash_indice = (hash_initial + probe**2) % self._capacity
            if self._buckets[hash_indice] and self._buckets[hash_indice].key == key:
                self._buckets[hash_indice].value = value
                if self._buckets[hash_indice].is_tombstone is True:
                    self._buckets[hash_indice].is_tombstone = False
                    self._size += 1
                break

            # add if not present
            if not self._buckets[hash_indice]:
                self._buckets[hash_indice] = HashEntry(key, value)
                self._size += 1
                break

            probe += 1

    def table_load(self) -> float:
        """return load factor"""
        return self._size / self._capacity

    def empty_buckets(self) -> int:
        """return empty indices"""

        count = 0
        for indice in range(self._capacity):

            # not using specific key, so any indice can be a key
            hash_initial = self._hash_function(str(indice)) % self._capacity
            pair = self._buckets.get_at_index(indice)
            if pair:

                # probe to find next empty bucket
                probe = 0
                while True:
                    if probe == self._capacity:
                        break

                    hash_indice = (hash_initial + probe ** 2) % self._capacity
                    if not self._buckets[hash_indice]:
                        break

                    probe += 1
            else:
                count += 1

        return count

    def resize_table(self, new_capacity: int) -> None:
        """
        change internal capacity;
        keep key-value pairs, rehash table links;
        return if input less than current length;
        else, ensure prime number;
        """

        if new_capacity < self._size:
            return

        # set capacity to next prime
        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)

        # similar to separate chaining, use put() with new buckets
        old_buckets, old_capacity = self._buckets, self._capacity

        self._buckets = DynamicArray()
        self._capacity, self._size = new_capacity, 0
        for _ in range(new_capacity):
            self._buckets.append(None)

        for key in range(old_capacity):
            pair = old_buckets.get_at_index(key)
            if pair and not pair.is_tombstone:
                self.put(pair.key, pair.value)

    def get(self, key: str) -> object:
        """return key value if present, else None"""

        # similar probing, except value return
        hash_initial = self._hash_function(key) % self._capacity
        probe = 0
        while True:
            if probe == self._capacity:
                break

            hash_indice = (hash_initial + probe**2) % self._capacity
            if self._buckets[hash_indice] and self._buckets[hash_indice].key == key:
                if self._buckets[hash_indice].is_tombstone is False:
                    return self._buckets[hash_indice].value

            probe += 1

    def contains_key(self, key: str) -> bool:
        """return True if key, else False"""

        # similar probing, except bool return
        hash_initial = self._hash_function(key) % self._capacity
        probe = 0
        while True:
            if probe == self._capacity:
                break

            hash_indice = (hash_initial + probe**2) % self._capacity
            if self._buckets[hash_indice] and self._buckets[hash_indice].key == key:
                return True

            probe += 1

        return False

    def remove(self, key: str) -> None:
        """remove key, value or nothing"""

        # similar probing, except tombstone value change
        hash_initial = self._hash_function(key) % self._capacity
        probe = 0
        while True:
            if probe == self._capacity:
                break

            hash_indice = (hash_initial + probe**2) % self._capacity
            if self._buckets[hash_indice] and self._buckets[hash_indice].key == key:
                if self._buckets[hash_indice].is_tombstone is False:
                    self._buckets[hash_indice].is_tombstone = True
                    self._size -= 1
                break

            probe += 1

    def clear(self) -> None:
        """clear table, keep capacity"""

        old_capacity = self._capacity

        self._buckets = DynamicArray()
        self._capacity, self._size = old_capacity, 0

        for indice in range(old_capacity):
            self._buckets.append(None)

    def get_keys_and_values(self) -> DynamicArray:
        """return dynamic array of key-value tuples"""

        array = DynamicArray()

        # similar probing, except append to new DA
        for indice in range(self._capacity):
            pair = self._buckets.get_at_index(indice)
            if pair and pair.is_tombstone is False:
                hash_initial = self._hash_function(pair.key) % self._capacity
                probe = 0
                while True:
                    if probe == self._capacity:
                        break

                    hash_indice = (hash_initial + probe**2) % self._capacity
                    if self._buckets[hash_indice] and self._buckets[hash_indice].is_tombstone is False:
                        array.append((pair.key, pair.value))
                        break

                    probe += 1

        return array

    def __iter__(self):
        """define, return hash-iterator object"""

        # similar to bag ADS
        self._index = 0
        return self

    def __next__(self):
        """return next bucket"""

        # loop if present
        while self._index < self._capacity:
            bucket = self._buckets[self._index]
            self._index += 1

            # only loops active items
            if bucket:
                return bucket

        # if no more buckets
        raise StopIteration

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

        if m.table_load() > 0.5:
            print(f"Check that the load factor is acceptable after the call to resize_table().\n"
                  f"Your load factor is {round(m.table_load(), 2)} and should be less than or equal to 0.5")

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
    m = HashMap(11, hash_function_1)
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

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.resize_table(2)
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(12)
    print(m.get_keys_and_values())

    print("\nPDF - __iter__(), __next__() example 1")
    print("---------------------")
    m = HashMap(10, hash_function_1)
    for i in range(5):
        m.put(str(i), str(i * 10))
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)

    print("\nPDF - __iter__(), __next__() example 2")
    print("---------------------")
    m = HashMap(10, hash_function_2)
    for i in range(5):
        m.put(str(i), str(i * 24))
    m.remove('0')
    m.remove('4')
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)
