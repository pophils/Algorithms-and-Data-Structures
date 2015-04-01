
from AppException.QueueException import QueueException
from AbstractBases.Queue import Queue as AbstractBaseQueue


class LinkedQueue(AbstractBaseQueue):

    class __Node:
        def __init__(self, e, nextNode):
            self.__element = e
            self.__nextNode = nextNode

        def nextNode(self, nextNode=None):
            if nextNode is None:
                return self.__nextNode
            else:
                self.__nextNode = nextNode

        def element(self):
            return self.__element

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def enqueue(self, e):

        newNode = self.__Node(e, None)

        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.nextNode(newNode)

        self.__tail = newNode
        self.__size += 1

    def dequeue(self):
        if self.isEmpty():
            raise QueueException("The queue is empty.")
        e = self.__head.element()
        self.__head = self.__head.nextNode()

        self.__size -= 1
        return e

    def isEmpty(self):
        return self.__size == 0

    def top(self):
        if self.isEmpty():
            raise QueueException("The queue is empty.")
        return self.__head.element()

    def clear(self):
        while self.__head is not None:
            self.__head = self.__head.nextNode()
        self.__size = 0

    def transfer(self, t=None):
        if self.isEmpty():
            raise QueueException("The queue is empty.")

        if t is not None and not isinstance(t, LinkedQueue):
            raise TypeError("The destination queue must be a proper Linked Queue type.")

        else:
            t = LinkedQueue()

        cursor = self.__head

        while cursor is not None:
            t.enqueue(cursor.element())
            cursor = cursor.nextNode()

        return t

    def toList(self):
        cursor = self.__head
        tempList = [None] * self.__size
        index = 0

        while cursor is not None:
            tempList[index] = cursor.element()
            cursor = cursor.nextNode()
            index += 1

        return tempList

    def __len__(self):
        return self.__size

    def size(self):
        return self.__size

    def __iter__(self):
        cursor = self.__head
        while cursor is not None:
            yield cursor.element()
            cursor = cursor.nextNode()