from math import ceil
from AbstractBases.Queue import Queue as AbstractBaseQueue
from AppException.QueueException import QueueException
from Chapter7_Linked_List.LinkedQueue import LinkedQueue


class ArrayQueue(AbstractBaseQueue):
    """
     Class implement an array based Queue ADT.
     Through an adapter design pattern, it makes use of
     built-in list and some of its attributes.

     All basic operations run in constant O(1) time complexity except for
     enqueue and dequeue that runs in amortized O(1) and occasional worst case
     O(n) time complexity when the underlying list has to be re-sized. n is the
     current size of the queue.
    """

    def __init__(self, capacity=10):
        """
        Init the queue with necessary attributes
        :param capacity: defaults to 10
        """
        self.__data = [None] * capacity
        self.__size = 0
        self.__front = 0
        self.__initCapacity = capacity

    def enqueue(self, item):
        """
        Add a new item to the queue.
        the underlying list is re-sized immediately before pushing
        the new item if the queue size is equal to the list capacity.
        :param item: item to be added.
        """
        if self.__size == len(self.__data):
            self.__resize(ceil(len(self.__data) * 2))

        # len() is called instead of currentLen cos the length of the __data might have changed due to resizing.
        nextEnqueueIndex = (self.__front + self.__size) % len(self.__data)
        self.__data[nextEnqueueIndex] = item

        self.__size += 1

    def dequeue(self):
        """
        Remove and return an item from the queue
        :return: object
        :exception: raises a QueueException if queue is empty
        """
        if self.isEmpty():
            raise QueueException("Queue is empty.")

        item = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__size -= 1
        self.__front = (self.__front + 1) % len(self.__data)

        if self.__isQueueDueForCompression():
            self.__resize(ceil(len(self.__data) * 2))

        return item

    def rotate(self, item):
        """
        See C-6.29: Function adds back a dequeued element into
        a queue. Unlike enqueue, its a constant time operation,
        since there is no need for resize operation.

        Raise a QueueException if the queue is already full to its
        capacity.
        """
        nextEnqueueIndex = (self.__front + self.__size) % len(self.__data)

        if self.__data[nextEnqueueIndex] is not None:
            raise QueueException("The queue is full to the capacity.")

        self.__data[nextEnqueueIndex] = item
        self.__size += 1

    def __resize(self, newCapacity):
        """
        Resize the queue. Its worst case running time is O(n)
        where n is the current size of the queue.
        :param newCapacity: New capacity of the queue
        """

        if not isinstance(newCapacity, int):
            raise TypeError("The new capacity is not an integer type.")

        tempData = [None] * newCapacity

        tempFront = self.__front

        for index in range(self.__size):
            tempData[index] = self.__data[tempFront]
            tempFront = (tempFront + 1) % len(self.__data)

        self.__data = tempData
        self.__front = 0

    def isEmpty(self):
        """
        Function checks if queue is empty.
        :return: boolean
        """
        return self.__size < 1

    def top(self):
        """
        Functions return the first item of the queue.
        :return: object
        :exception: raises a QueueException if queue is empty
        """
        if self.isEmpty():
            raise QueueException("Queue is empty.")
        return self.__data[self.__front]

    def clear(self):
        """
        Clear all the element of the queue
        """
        self.__data = [None] * self.__initCapacity
        self.__size = 0
        self.__front = 0

    def size(self):
        return self.__size

    def __iter__(self):
        tempFront = self.__front
        for index in range(self.__size):
            yield self.__data[tempFront]
            tempFront = (tempFront + 1) % len(self.__data)

    def transfer(self, t=None):
        """
         R-6.3 Transfer the element of this stack to a new queue.
        :param t: Destination Queue
        :return: The destination queue
        """
        if self.isEmpty():
            raise QueueException("The source queue is empty")

        if t is None:
            t = ArrayQueue(self.__size)
        else:
            if not isinstance(t, ArrayQueue):
                raise QueueException("The destination is not a queue type")

        tempFront = self.__front
        for index in range(self.__size):
            t.enqueue(self.__data[tempFront])
            tempFront = (tempFront + 1) % len(self.__data)

        return t

    def toList(self):
        """
        Returns a list of the queue items
        :return: list
        """
        tempList = [None] * self.__size
        tempFront = self.__front

        for index in range(self.__size):
            tempList[index] = self.__data[tempFront]
            tempFront = (tempFront + 1) % len(self.__data)
        return tempList

    def __len__(self):
        """
        Function return the size of the queue
        :return: int
        """
        return self.__size

    def __isQueueDueForCompression(self):
        """
        Checks if the Queue size could be reduced after dequeueing the top.
        :return: boolean
        """
        return self.__size <= (len(self.__data) // 4)

    def __str__(self):
        """
        ToString() of Queue object
        :return: str
        """
        return 'Am a Queue object with %s element(s)' % self.__size


if __name__ == '__main__':
    q = ArrayQueue(5)

    print("Queue size: %s" % len(q))
    print("-------------------------------------")
    print("-------------------------------------")

    q.enqueue(20)
    q.enqueue(200)
    q.enqueue(2000)
    q.enqueue(20000)
    q.enqueue({1: 1, 2: 'huffman code', 3: 'Star wars'})
    q.enqueue(20111)
    q.enqueue(2001111)

    print("Queue size: %s" % len(q))
    print("Top of Queue: %s" % q.top())
    print("-------------------------------------")
    print("-------------------------------------")
    print(q.toList())

    q.dequeue()
    q.dequeue()
    q.dequeue()

    print("Queue size: %s" % len(q))
    print("Top of Queue: %s" % q.top())
    print("-------------------------------------")
    print("-------------------------------------")

    print(q.toList())

    for i in q:
        print(type(i))
        print(i)