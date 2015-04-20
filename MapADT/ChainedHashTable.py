
from AbstractBases.HashTable import HashTable as hashTableBase
from MapADT.UnsortedMap import UnsortedMap


class ChainedHashTable(hashTableBase):

    def __setitem__(self, k, value):
        bucketIndex = self._hashFunction(k)
        if self._table[bucketIndex] is None:
            self._table[bucketIndex] = UnsortedMap()

        oldLen = len(self._table[bucketIndex])
        self._table[bucketIndex][k] = value

        if oldLen != len(self._table[bucketIndex]):
            self._size += 1

        if self._size / len(self._table) > self._loadFactor:
            if len(self._table) < 50000:
                self._resize(len(self._table) * 3)
            else:
                self._resize(len(self._table) * 2)

    def __getitem__(self, k):
        bucketIndex = self._hashFunction(k)

        if self._table[bucketIndex] is None:
            raise KeyError("KeyError: " + repr(k))
        return self._table[bucketIndex][k]

    def __delitem__(self, k):
        bucketIndex = self._hashFunction(k)
        if self._table[bucketIndex] is None:
            raise KeyError("KeyError: " + repr(k))
        del self._table[bucketIndex][k]
        self._size -= 1

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key


if __name__ == '__main__':
    d = ChainedHashTable()

    d['microsoft'] = 'c#'
    d['oracle'] = 'java'
    d['google'] = 'go'
    d['apple'] = 'swift'
    d['yahoo'] = 'YUI'
    d['mozilla'] = 'javascript'
    d['google2'] = 'angularJS'
    d['square'] = 'picasso'

    for j in d.items():
        print(j)

    print(len(d))

