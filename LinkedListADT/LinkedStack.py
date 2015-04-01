
from AbstractBases.Stack import Stack
from AppException.StackException import StackException


class LinkedStack(Stack):

    def __len__(self):
        return self.__size

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
        self.__size = 0
        self.__head = None

    def push(self, e):
        self.__head = self.__Node(e, self.__head)
        self.__size += 1

    def pop(self):
        if self.isEmpty():
            raise StackException("The stack is empty.")
        e = self.__head.element()
        self.__head = self.__head.nextNode()
        self.__size -= 1

        return e

    def top(self):
        if self.isEmpty():
            raise StackException("The stack is empty.")

        return self.__head.element()

    def isEmpty(self):
        return self.__size == 0

    def transfer(self, t=None):
        if self.isEmpty():
            raise StackException("The stack is empty.")

        if t is not None and not isinstance(t, LinkedStack):
            raise TypeError("The destination stack must be a proper Linked Stack type.")

        else:
            t = LinkedStack()

        tempList = self.toList()

        for cursor in range(self.__size):
            t.push(tempList.pop())

        return t

    def clear(self):
        while self.__head is not None:
            self.__head = self.__head.nextNode()
        self.__size = 0

    def size(self):
        return self.__size

    def __iter__(self):
        cursor = self.__head
        while cursor is not None:
            yield cursor.element()
            cursor = cursor.nextNode()

    def toList(self):
        cursor = self.__head
        tempList = [None] * self.__size
        index = 0

        while cursor is not None:
            tempList[index] = cursor.element()
            cursor = cursor.nextNode()
            index += 1

        return tempList