
class QueueException(Exception):
    """
    Used with the Queue class to manage exception
    """
    pass

from math import ceil

class Queue():
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
        :return:
        """
        self.__data = [None] * capacity
        self.__size = 0
        self.__front = 0

    def enqueue(self, item):
        if self.__size == len(self.__data):
            self.__resize(ceil(self.__size * 2.5))

        # len() is called instead of currentLen cos the length of the __data might have changed due to resizing.
        nextEnqueueIndex = (self.__front + self.__size) % len(self.__data)
        self.__data[nextEnqueueIndex] = item

        self.__size += 1

    def dequeue(self):

        if self.isEmpty():
            raise QueueException("Queue is empty.")

        item = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__size -= 1
        self.__front = (self.__front + 1) % len(self.__data)

        if self.__isQueueDueForCompression():
            self.__resize(ceil(self.__size * 1.5))

        return item

    def __resize(self, newCapacity):

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
        return self.__size < 1

    def top(self):
        if self.isEmpty():
            raise QueueException("Queue is empty.")
        return self.__data[self.__front]

    def __len__(self):
        return self.__size

    def __isQueueDueForCompression(self):
        """
        Checks if the Queue size could be reduced after dequeueing the top.
        :return: boolean
        """
        return self.__size <= (len(self.__data)//4)

    def __str__(self):
        return 'Am a Queue object with %s element' % self.__size

if __name__ == '__main__':
    q = Queue(5)

    print("Queue size: %s" % len(q))
    print("-------------------------------------")
    print("-------------------------------------")

    q.enqueue(20)
    q.enqueue(200)
    q.enqueue(2000)
    q.enqueue(20000)
    q.enqueue(20111)
    q.enqueue(2001111)

    print("Queue size: %s" % len(q))
    print("Top of Queue: %s" % q.top())
    print("-------------------------------------")
    print("-------------------------------------")

    q.dequeue()
    q.dequeue()
    q.dequeue()

    print("Queue size: %s" % len(q))
    print("Top of Queue: %s" % q.top())
    print("-------------------------------------")
    print("-------------------------------------")