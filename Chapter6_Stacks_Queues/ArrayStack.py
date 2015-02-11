class StackException(Exception):
    """
    Used with the Stack class to manage exception
    """
    pass


class Stack():
    """
     Class implement an array based Stack ADT.
     Through an adapter design pattern, it makes use of
     built-in list and some of its attributes.
    """

    def __init__(self, capacity=None):
        """
        Init the stack with appropriate attributes
        :param capacity: The capacity of the stack. Its optional.
        :exception: Raises stackException if capacity given is not an integer
        """
        if capacity is None:
            self.__data = []
        else:
            if not isinstance(capacity, int):
                raise StackException("The size attribute must be an integer.")

            self.__data = [None] * capacity
            self.__size = 0
            self.__capacityGiven = True

    def push(self, item):
        """
        Push a new item to the stack.
        if capacity of the stack is given at init, the stack is
        re-sized immediately before pushing new item if the stack
        size is equal to the capacity.
        :param item: Item to be pushed to the stack
        :return: void
        """
        currentLen = len(self.__data)
        if currentLen == self.__size:
            self.__resize(currentLen*2)

        self.__data[self.__size] = item
        self.__size += 1

    def pop(self):
        """
        Remove and return the last item of the stack.
        Resize underlying list if the size of the stack is
        less or equal a quarter of its length
        :return: Object
        :exception: Raises a StackException if stack is empty.
        """
        if self.isEmpty():
            raise StackException("The stack is empty.")

        item = self.__data.pop()

        if self.isStackDueForCompression():
            self.__resize(len(self.__data)//2)

        self.__size -= 1
        return item

    def __resize(self, newCapacity):
        """
        Resize the stack.
        :param newCapacity: New capacity of the stack
        :return:void
        """
        oldData = [None] * newCapacity
        for index in range(self.__size):
            oldData[index] = self.__data[index]

        self.__data = oldData

    def isStackDueForCompression(self):
        return self.__size <= (len(self.__data)//4)

    def isEmpty(self):
        """
        Checks if the stack is empty.
        :return: Boolean
        """
        return self.__size == 0

    def dataLen(self):
        return len(self.__data)

    def __str__(self):
        return 'Am a stack object with %s element' % self.__size

    def __len__(self):
        """
        :return:Current size of the stack
        """
        return self.__size

    def __getitem__(self, index):
        """
        An indexer for returning element of the stack
        :param index: Index of the stack to return
        :return: returns an element of the stack.
        """
        if self.isEmpty():
            raise StackException("The stack is empty")
        if not isinstance(index, int):
            raise StackException("Index must be nothing but an integer")
        if abs(index) >= self.__size:
            raise StackException("Index is out of range")

        self.__data.count()
        return self.__data[index]

    def transfer(self, T=None):

        """
         R-6.3 Transfer the element of this stack to a destination stack.
        :param T: Destination Stack
        :return: The destination stack
        """

        if self.isEmpty():
            raise StackException("The source stack is empty")

        if T is None:
            T = Stack(self.__size)
        else:
            if not isinstance(T, Stack):
                raise StackException("The destination is not a stack type")

        for index in range(self.__size):
            T.push(self.pop())

        return T


if __name__ == '__main__':
    s1 = Stack(10)
    print("Stack size: %s" % len(s1))
    print("Internal data len: %s" % s1.dataLen())
    print("-------------------------------------")
    print("-------------------------------------")
    s1.push(3)
    s1.push(20)
    s1.push('Kolapo')
    s1.push(200)
    print("Stack size: %s" % len(s1))
    print("Internal data len: %s" % s1.dataLen())
    print("-------------------------------------")
    print("-------------------------------------")
