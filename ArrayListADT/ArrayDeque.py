

from AbstractBases.Deque import Deque as AbstractBaseDeque
from AppException.DequeException import DequeException
from math import ceil


class ArrayDeque(AbstractBaseDeque):
    """
    Class implement an array based Deque otherwise known as a Double-ended Queue ADT. It use the
    concept of circular array for the underlying storage.
    """
    __DefaultCapacity = 50  # Chosen arbitrarily
    __maxLenGiven = False

    def __init__(self, maxLen=None):

        if maxLen is not None:
            if not isinstance(maxLen, int):
                raise TypeError("maxLen is not an integer")
            if maxLen < 1:
                raise ValueError("maxLen must be greater than 0.")
            self.__DefaultCapacity = maxLen
            self.__maxLenGiven = True

        self.__data = [None] * self.__DefaultCapacity
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def append(self, e):
        """
        If maximum capacity is not given, it runs in amortized O(1) time and occasionally O(n) times if there is a need
        for resizing the underlying list.
        Runs in constant time O(1) complexity if the maximum capacity is given.
        If the maximum capacity is given and it has been reached, the deque is adjusted
        such that the first element is removed leaving the second element as the new
        head and the newly appended element as the tail of the deque.
        :param e: Item to be appended
        """
        if not self.__maxLenGiven:
            if self.__size == len(self.__data):
                self.__resize(len(self.__data) * 2.5)

            if not self.isEmpty():
                self.__tail = (self.__tail + 1) % len(self.__data)

            self.__data[self.__tail] = e
            self.__size += 1
        else:
            if self.__size < self.__DefaultCapacity:
                if not self.isEmpty():
                    self.__tail = (self.__tail + 1) % len(self.__data)

                self.__data[self.__tail] = e
                self.__size += 1
            else:
                self.__data[self.__head] = e
                self.__head = (self.__head + 1) % len(self.__data)
                self.__tail = (self.__tail + 1) % len(self.__data)

    def appendLeft(self, e):
        """
        If maximum capacity is not given, it runs in amortized O(1) time and occasionally O(n) times if there is a need
        for resizing the underlying list.
        Runs in constant time O(1) complexity if the maximum capacity is given.
        If the maximum capacity is given and has been reached, the deque is adjusted
        such that the last element is removed leaving the penultimate element as the new
        tail and the newly appended element as the head of the deque.
        :param e: Item to be appended
        """
        if not self.__maxLenGiven:
            if self.__size == len(self.__data):
                self.__resize(len(self.__data) * 2.5)

            if not self.isEmpty():
                self.__head = (self.__head - 1) % len(self.__data)

            self.__data[self.__head] = e
            self.__size += 1
        else:
            if self.__size < self.__DefaultCapacity:
                if not self.isEmpty():
                    self.__head = (self.__head - 1) % len(self.__data)

                self.__data[self.__head] = e
                self.__size += 1
            else:
                self.__data[self.__tail] = e
                self.__head = (self.__head - 1) % len(self.__data)
                self.__tail = (self.__tail - 1) % len(self.__data)

    def pop(self):
        """
        Runs in amortized O(1) time. Occasionally O(n) times if there is a need for resizing the underlying list.
        Runs in constant O(1) time if maximum capacity is given during instantiation.
        """
        if self.isEmpty():
            raise DequeException("The deque is empty.")
        e = self.__data[self.__tail]
        self.__data[self.__tail] = None
        self.__tail = (self.__tail - 1) % len(self.__data)

        self.__size -= 1

        if self.__isDequeDueForCompression():
            self.__resize(len(self.__data) * 2)

        return e

    def popLeft(self):
        """
        Runs in amortized O(1) time. Occasionally O(n) times if there is a need for resizing the underlying list.
        Runs in constant O(1) time if maximum capacity is given during instantiation.
        """
        if self.isEmpty():
            raise DequeException("The deque is empty.")
        e = self.__data[self.__head]
        self.__data[self.__head] = None
        self.__head = (self.__head + 1) % len(self.__data)

        self.__size -= 1

        if self.__isDequeDueForCompression():
            self.__resize(len(self.__data) * 2)

        return e

    def clear(self):
        """
        Runs in constant O(1) time.
        """
        self.__data = [None] * self.__DefaultCapacity
        self.__size = 0
        self.__head = 0
        self.__tail = 0

    def rotate(self, k):
        """
        Runs in O(k) worst case time.
        :param k: number of times to rotate the deque
        """
        if not isinstance(k, int):
            raise TypeError("k must be an integer.")

        if self.isEmpty():
            raise DequeException("Deque is empty.")

        for index in range(k):
            currentItem = self.__data[self.__head]
            self.__data[self.__head] = None
            self.__head = (self.__head + 1) % len(self.__data)
            self.__tail = (self.__tail + 1) % len(self.__data)
            self.__data[self.__tail] = currentItem

    def size(self):
        """
        Runs in O(1) worst case time.
        """
        return self.__size

    def toList(self):
        """
        Runs in O(n) worst case time.
        """
        tempList = [None] * self.__size
        headCursor = self.__head

        for cursor in range(self.__size):
            tempList[cursor] = self.__data[headCursor]
            headCursor = (headCursor + 1) % len(self.__data)

        return tempList

    def remove(self, e):
        """
        Removes the first occurrence of item e in the deque.
        Runs in O(n) worst case time.
        :param e: item to be removed
        """
        if self.isEmpty():
            raise DequeException("The deque is empty.")
        try:
            self.__data.remove(e)
        except ValueError:
            raise ValueError("e not in deque")

    def count(self, e):
        """
        Count the number of matches for e in the deque.
        Runs in O(n) worst case time.
        :param e: item to be removed
        """
        if self.isEmpty():
            raise DequeException("The deque is empty.")

        return self.__data.count(e)

    def isEmpty(self):
        """
        Runs in O(1) worst case time.
        """
        return self.__size == 0

    def __resize(self, newCapacity):
        """
        Runs in O(n) worst case time. where n is the current size of the deque
        """
        if self.isEmpty():
            raise DequeException("You cannot resize an empty deque.")

        newDataList = [None] * ceil(newCapacity)
        headCursor = self.__head

        for cursor in range(self.__size):
            newDataList[cursor] = self.__data[headCursor]
            headCursor = (headCursor + 1) % len(self.__data)

        self.__data = newDataList
        self.__head = 0
        self.__tail = self.__size - 1

    def __isDequeDueForCompression(self):
        """
        Checks if the Deque size could be reduced after removing any item from it.
        Runs O(1) time.
        :return: boolean
        """
        return self.__size <= (len(self.__data) // 4)

    def __iter__(self):
        """
        Runs in O(n) worst case time.
        """
        headCursor = self.__head

        for cursor in range(self.__size):
            yield self.__data[headCursor]
            headCursor = (headCursor + 1) % len(self.__data)

    def __len__(self):
        """
        Runs in O(1) worst case time.
        """
        return self.__size

    def __getitem__(self, index):
        """
        Runs in O(1) worst case time.
        :param index: index of the item to return
        :exception IndexError, TypeError: raise an exception if index is not an integer or is more than or equal to size of deque
        """
        if not isinstance(index, int):
            raise TypeError("index must be an integer")
        if index >= 0 and index >= self.__size:
            raise IndexError("deque index out of range")
        if index < 0 and abs(index) > self.__size:
            raise IndexError("deque index out of range")

        if index >= 0:
            return self.__data[(self.__head + index) % len(self.__data)]
        else:
            return self.__data[(self.__tail - abs(index) + 1) % len(self.__data)]

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("index must be an integer")
        if index >= 0 and index >= self.__size:
            raise IndexError("deque index out of range")
        if index < 0 and abs(index) > self.__size:
            raise IndexError("deque index out of range")

        if index >= 0:
            self.__data[(self.__head + index) % len(self.__data)] = value
        else:
            self.__data[(self.__tail - abs(index) + 1) % len(self.__data) ] = value


if __name__ == '__main__':
    s1 = ArrayDeque(4)

    s1.appendLeft(3)
    s1.appendLeft(20)
    s1.append(200)

    print("Deque size: %s" % len(s1))
    print(s1.toList())

    s1.appendLeft(303)
    print("Deque size: %s" % len(s1))
    print(s1.toList())

    s1.append(2003)
    s1.appendLeft(20003)

    print("Deque size: %s" % len(s1))
    print(s1.toList())

    s1.pop()
    s1.appendLeft(30000)
    s1.appendLeft(300000)

    print("Deque size: %s" % len(s1))
    print(s1.toList())

    s1.append(40000)
    s1.append(400000)

    print("Deque size: %s" % len(s1))
    print(s1.toList())

    s1.append(50000)
    s1.popLeft()
    s1.appendLeft(500000)

    print("Deque size: %s" % len(s1))
    print(s1.toList())

    s1.append(50000)
    s1.append(60000)
    s1.appendLeft(500000)

    print("Deque size: %s" % len(s1))
    print(s1.toList())