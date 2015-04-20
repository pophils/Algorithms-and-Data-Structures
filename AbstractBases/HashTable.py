
from AbstractBases.Map import Map as abstractMapBase
from random import randrange


class HashTable(abstractMapBase):
    """
    Abstract class for an HashTable.
    Class could be implemented to provide the various collision
    resolution strategies e.g Separate chaining, Linear probing,
    Quadratic probing, Double hashing, Cuckoo hashing and what a view.

    Hash values are generated using builtin hash() in python.
    Compression function is based on MAD strategy to eliminate repeated pattern
    in hash values;
    [(ai+b) mod p] mod N where Nis the table size and p is a prime number larger than N.
    a is chosen randomly from 1 - N ( a must not be zero as this will make the
    compression function goes into an infinite loop), likewise b is chosen randomly from 0 - N
    """

    def __init__(self, load_factor=0.5, table_size=11, p =137):
        if not (isinstance(load_factor, int) or isinstance(load_factor, float)):
            raise TypeError("load factor must be a number.")
        if not isinstance(table_size, int):
            raise TypeError("table_size must be an integer.")

        self._table = [None] * table_size
        self._loadFactor = load_factor
        self._size = table_size
        self.__a = randrange(1, p)
        self.__b = randrange(0, p)
        self.__p = p

    def _hashFunction(self, k):
        return (hash(k) * self.__a + self.__b) % self.__p % len(self._table)

    def _resize(self, newCapacity):
        print('resizing')
        oldItems = list(self.items())
        self._table = [None] * newCapacity
        self._size = 0

        for (k,v) in oldItems:
            self[k] = v

    def __len__(self):
        return self._size

    def clear(self):
        self._table = []
        self._size = 0