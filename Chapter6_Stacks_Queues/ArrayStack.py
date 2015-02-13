class StackException(Exception):
    """
    Used with the Stack class to manage exception
    """
    pass

from math import ceil

class Stack():
    """
     Class implement an array based Stack ADT.
     Through an adapter design pattern, it makes use of
     built-in list and some of its attributes.

     All basic operations run in constant O(1) time complexity except for
     pop and push that runs in amortized O(1) and occasional worst case
     O(n) time complexity when the underlying list has to be re-sized. n is the
     current size of the stack.
    """

    def __init__(self, capacity=None):
        """
        Init the stack with appropriate attributes
        :param capacity: The capacity of the stack. Its optional.
        :exception: Raises StackException if capacity given is not an integer.
        """
        if capacity is None:
            self.__data = []
            self.__capacityGiven = False
        else:
            if not isinstance(capacity, int):
                raise StackException("The size attribute must be an integer.")

            self.__data = [None] * capacity
            self.__capacityGiven = True
        self.__size = 0
        self.__front = 0

    def push(self, item):
        """
        Push a new item to the stack.
        if capacity of the stack is given at init, the underlying list is
        re-sized immediately before pushing the new item if the stack size
        is equal to the list capacity.
        :param item: Item to be pushed to the stack
        """
        if self.__capacityGiven:
            if len(self.__data) == self.__size:
                self.__resize(ceil(self.__size*2.5))
            self.__data[self.__size] = item

        else:
            self.__data.append(item)

        self.__size += 1
        self.__front = self.__size - 1

    def pop(self):
        """
        Remove and return the last item of the stack.
        Resize underlying list if the size of the stack is
        less or equal to quarter of its length
        :return: Object
        :exception: Raises a StackException if stack is empty.
        """
        if self.isEmpty():
            raise StackException("The stack is empty.")

        if self.__capacityGiven:
            item = self.__data[self.__front]
            self.__data[self.__front] = None

            if self.isStackDueForCompression():
                self.__resize(ceil(self.__size*1.5))
        else:
            item = self.__data.pop()

        self.__size -= 1
        self.__front = self.__size - 1
        return item

    def top(self):
        if self.isEmpty():
            raise StackException("The stack is empty.")
        return self.__data[self.__size-1]

    def size(self):
        return self.__size

    def __resize(self, newCapacity):
        """
        Resize the stack. Its worst case running time is O(n)
        where n is the current size of the stack.
        :param newCapacity: New capacity of the stack
        """
        if not isinstance(newCapacity, int):
            raise TypeError("The new capacity is not an integer.")

        tempData = [None] * newCapacity
        for index in range(self.__size):
            tempData[index] = self.__data[index]

        self.__data = tempData

    def isStackDueForCompression(self):
        """
        Checks if the stack size could be reduced after popping the head.
        :return: boolean
        """
        return self.__size <= (len(self.__data)//4)

    def isEmpty(self):
        """
        Checks if the stack is empty.
        :return: boolean
        """
        return self.__size == 0

    def __str__(self):
        return 'Am a stack object with %s element' % self.__size

    def __len__(self):
        """
        :return:Current size of the stack.
        """
        return self.__size

    def transfer(self, t=None):

        """
         R-6.3 Transfer the element of this stack to a destination stack.
        :param t: Destination Stack
        :return: The destination stack
        """

        if self.isEmpty():
            raise StackException("The source stack is empty")

        if t is None:
            t = Stack(self.__size)
        else:
            if not isinstance(t, Stack):
                raise StackException("The destination is not a stack type")

        for index in range(self.__size):
            t.push(self.pop())

        return t


if __name__ == '__main__':
    s1 = Stack(1)
    print("Stack size: %s" % s1.size())
    print("-------------------------------------")
    print("-------------------------------------")
    s1.push(3)
    s1.push(20)
    s1.push(200)
    print("Stack size: %s" % s1.size())
    print("-------------------------------------")
    print("-------------------------------------")
    print("Top of stack: %s" % s1.top())
    s1.pop()
    print("-------------------------------------")
    print("-------------------------------------")
    print("Stack size: %s" % s1.size())
    print("Top of stack: %s" % s1.top())
