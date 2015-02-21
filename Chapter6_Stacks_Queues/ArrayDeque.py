

from AbstractBases.Deque import Deque as AbstractBaseDeque
from AppException.DequeException import DequeException
from math import ceil


class ArrayDeque(AbstractBaseDeque):
    """
    P-6.32: Class implement an array based Double-ended Queue ADT.
    """
    __DefaultCapacity = 50

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
        Runs in amortized O(1) time. Occasionally O(n) times if there is a resizing.
        :param e: Item to be appended
        """

        if self.__size == len(self.__data):
            self.__resize(self.__size * 2.5)

        self.__tail = (self.__tail + 1) % len(self.__data)
        self.__data[self.__tail] = e

        self.__size += 1

    def __resize(self, newCapacity):

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

    def appendLeft(self, e):
        """
        This will take O(2n) worst case time where n is the current size of the queue
        :param e: item to be appended
        """
        if self.__size == len(self.__data):
            self.__resize(self.__size * 2.5)

        self.__head = (self.__head - 1) % len(self.__data)
        self.__data[self.__head] = e

        self.__size += 1

    def pop(self):
        """
        Runs in constant O(1) time.
        :return: Object
        """
        if self.isEmpty():
            raise DequeException("The deque is empty.")
        e = self.__data[self.__tail]
        self.__data[self.__tail] = None
        self.__tail = (self.__tail - 1) % len(self.__data)

        self.__size -= 1

        if self.__isDequeDueForCompression():
            self.__resize(self.__size * 1.5)

        return e

    def popLeft(self):
        """
        This will take O(2n) worst case time where n is the current size of the queue
        :return: object
        """
        if self.isEmpty():
            raise DequeException("The deque is empty.")
        e = self.__data[self.__head]
        self.__data[self.__head] = None
        self.__head = (self.__head + 1) % len(self.__data)

        self.__size -= 1

        if self.__isDequeDueForCompression():
            self.__resize(self.__size * 1.5)

        return e

    def __isDequeDueForCompression(self):
        """
        Checks if the Deque size could be reduced after removing any item from it.
        :return: boolean
        """
        return self.__size <= (len(self.__data) // 4)

    def clear(self):
        self.__data = [None] * self.__DefaultCapacity
        self.__size = 0
        self.__head = 0
        self.__tail = 0

    def rotate(self, k):
        """
        Runs in O(2kn) worst case time.
        :param k:
        """
        if not isinstance(k, int):
            raise TypeError("k must be an integer.")

        if self.isEmpty():
            raise DequeException("Deque is empty.")

        for index in range(k):
            self.__tail = self.__head
            self.__head = (self.__head + 1) % len(self.__data)

    def size(self):
        return self.__size

    def toList(self):
        tempList = [None] * self.__size
        headCursor = self.__head

        for cursor in range(self.__size):
            tempList[cursor] = self.__data[headCursor]
            headCursor = (headCursor + 1) % len(self.__data)

        return tempList

    def __iter__(self):
        headCursor = self.__head

        for cursor in range(self.__size):
            yield self.__data[headCursor]
            headCursor = (headCursor + 1) % len(self.__data)

    def __len__(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0


if __name__ == '__main__':
    s1 = ArrayDeque()

    s1.append(3)
    s1.append(20)
    s1.append(200)

    print("Stack size: %s" % len(s1))
    print(s1.toList())

    s1.appendLeft(30)
    s1.appendLeft([1, 3, 5, 7, 'google'])

    print("Stack size: %s" % len(s1))
    print(s1.toList())

    s1.pop()

    print("Stack size: %s" % len(s1))
    print(s1.toList())

    s1.appendLeft(111111)
    s1.append(11111111)
    s1.append((12, 13, 24, 'kmeans'))

    print("Stack size: %s" % len(s1))
    print(s1.toList())

    s1.append(False)

    print("Stack size: %s" % len(s1))
    print(s1.toList())

    s1.popLeft()
    s1.popLeft()
    s1.popLeft()

    print("Stack size: %s" % len(s1))
    print(s1.toList())