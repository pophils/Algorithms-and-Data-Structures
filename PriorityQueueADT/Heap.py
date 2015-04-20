
from AbstractBases.PriorityQueue import PriorityQueue as abstractPQ
from AppException.PriorityQueueException import PriorityQueueException


class Heap(abstractPQ):
    """
    Class implements a binary heap.
    It makes use of a complete binary tree such that the
    parent value is more than the children values or vice versa for
    a max and min priority configuration respectively.
    """

    def __init__(self, order=0, dType=int):

        if not isinstance(order, int):
            raise TypeError("order must be an integer")

        if order == 0:
            self.__isMin = True
        else:
            self.__isMin = False

        self.__data = []
        self.__dType = dType


    def __validateDType(self, e):
        if not isinstance(e, self.__dType):
            raise TypeError("e must be of %s" % self.__dType)

    def __left(self, i):
        return 2 * i + 1

    def __right(self, i):
        return 2 * i + 2

    def __parent(self, i):
        if i <= 0:
            return 0
        else:
            return (i - 1) // 2

    def __hasLeft(self, i):
        return self.__left(i) < len(self.__data)

    def __hasRight(self, i):
        return self.__right(i) < len(self.__data)

    def __swap(self, i, j):
        self.__data[i], self.__data[j] = self.__data[j], self.__data[i]

    def insert(self, e):
        self.__validateDType(e)
        self.__data.append(e)
        self.__percolateUp(len(self.__data) - 1)

    def removeTop(self):
        if self.isEmpty():
            raise PriorityQueueException("The heap is empty.")

        self.__swap(0, len(self.__data) - 1)
        top = self.__data.pop()
        self.__percolateDown(0)

        return top

    def heapify(self, l):
        if not isinstance(l, list):
            raise TypeError("l must be a list of objects.")

        if len(l) < 1:
            raise ValueError("l is empty.")

        self.__data = l

        lastParent = self.__parent(len(self.__data) - 1)

        for cursor in range(lastParent, -1, -1):
            self.__percolateDown(cursor)

    def __percolateDown(self, i):
        if self.__hasLeft(i):

            right = None
            if self.__hasRight(i):
                    right = self.__right(i)

            if self.__isMin:
                smallestChild = self.__left(i)
                if right is not None and self.__data[right] < self.__data[smallestChild]:
                    smallestChild = right

                if self.__data[i] > self.__data[smallestChild]:
                    self.__swap(smallestChild, i)
                    self.__percolateDown(smallestChild)
            else:
                biggestChild = self.__left(i)
                if right is not None and self.__data[right] > self.__data[biggestChild]:
                        biggestChild = right

                if self.__data[i] < self.__data[biggestChild]:
                    self.__swap(biggestChild, i)
                    self.__percolateDown(biggestChild)

    def __percolateUp(self, i):
        parent = self.__parent(i)
        if self.__isMin:
            if i > 0 and self.__data[i] < self.__data[parent]:
                self.__swap(i, parent)
                self.__percolateUp(parent)
        else:
            if i > 0 and self.__data[i] > self.__data[parent]:
                self.__swap(i, parent)
                self.__percolateUp(parent)

    def clear(self):
        self.__data = []

    def peekTop(self):
        if self.isEmpty():
            raise PriorityQueueException("The heap is empty.")
        return self.__data[0]

    def isEmpty(self):
        return len(self.__data) == 0

    def __len__(self):
        return len(self.__data)

    def size(self):
        return len(self.__data)


if __name__ == '__main__':

    heap = Heap(order=0, dType=str)

    a = ['google', 'west','yahoo']

    for i in range(len(a)):
        heap.insert(a[i])

    b = [heap.removeTop() for i in range(len(heap))]

    print(a)
    print(b)