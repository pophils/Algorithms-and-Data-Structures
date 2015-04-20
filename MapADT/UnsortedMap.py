
from AbstractBases.Map import Map as abstractMapBase

class UnsortedMap(abstractMapBase):

    def __init__(self):
        self.__table = []

    def __setitem__(self, k, value):
        for item in self.__table:
            if item._key == k:
                item._value = value
                return
        self.__table.append(self._Item(k, value))

    def __getitem__(self, k):
        for item in self.__table:
            if item._key == k:
                return item._value

        raise KeyError("KeyError: " + repr(k))

    def __delitem__(self, k):
        for cursor in range(len(self.__table)):
            if self.__table[cursor]._key == k:
                self.__table.pop(cursor)
                return
        raise KeyError("KeyError: " + repr(k))

    def __len__(self):
        return len(self.__table)

    def __iter__(self):
        for item in self.__table:
            yield item._key

    def isEmpty(self):
        return len(self.__table) == 0

    def clear(self): # runs in O(1) unlike the one implemented in super class.
        self.__table = []



if __name__ == '__main__':

    d = UnsortedMap()

    d[1] = 23
    d[12] = 1234
    d['dict1'] = 111

    print(len(d))
    del d[1]
    print(len(d))

    d.clear()

    for i in d.keys():
        print(i)



