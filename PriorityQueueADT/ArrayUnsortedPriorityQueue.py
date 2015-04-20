
from AbstractBases.PriorityQueue import PriorityQueue as abstractPQ
from AppException.PriorityQueueException import PriorityQueueException

class ArrayUnsortedPriorityQueue(abstractPQ):
    """
    Class implement an unsorted priority Queue.
    All items are added arbitrarily in constant O(1) time without following
    any order.
    To remove the head item, a scan is done to locate the item
    with the highest or lowest priority depending on the configuration
    of the Queue i.e(min or max priority queue). The removal process will involve
    scanning from the front of the array to the item index and a backward shift of all elements after
    the item in question is removed. This make it runs in Omega(n) time.
    """

    def __init__(self, order=0, capacity=None, itemType=int):
        """
        Init the queue
        :param order: The order at which items are removed from the queue. 0=Min, 1=Max
        """
        if not isinstance(order, int):
            raise TypeError("order must be a number.")
        if capacity is not None and not isinstance(order, int):
            raise TypeError("capacity must be a number.")

        self.__capacityGiven = False
        self.__data = []
        self.__itemType = itemType
        self.__currentHead = 0

        if order > 0:
            self.__isMin = False
        else:
            self.__isMin = True

        if capacity is not None:
            self.__capacityGiven = True
            self.__capacity = capacity

    def __validateItemType(self, e):
        """
        Validate each item type against the supplied type at __init__
        :param e: item
        """
        if type(e) != self.__itemType:
            raise TypeError("element of the queue must be of the type %s" % self.__itemType)

    def insert(self, e):
        """
        Insert new item to the priority queue
        Runs in constant O(1) time
        :param e: item to be added
        :exception raise a PriorityQueueException if the capacity is given at instantiation and the
                   current size of the queue is equals the given capacity.
        """
        self.__validateItemType(e)

        if self.__capacityGiven:
            if len(self.__data) == self.__capacity:
                raise PriorityQueueException("The queue is already full.")


        self.__data.append(e)

        if self.__isMin:
            if self.__data[self.__currentHead] > self.__data[len(self.__data) - 1]:
                self.__currentHead = len(self.__data) - 1
        else:
            if self.__data[self.__currentHead] < self.__data[len(self.__data) - 1]:
                self.__currentHead = len(self.__data) - 1

    def removeTop(self):
        """
        Removes the head of the queue. Runs in Omega(n) time.
        :return: Object
        :exception raise PriorityQueueException if queue is empty
        """

        if self.isEmpty():
            raise PriorityQueueException("The queue is empty.")

        if self.__isMin:

            min = self.__data[self.__currentHead]
            del self.__data[self.__currentHead]

            smallest = self.__data[0]
            self.__currentHead = 0

            for cursor in range(len(self.__data) - 1):
                if smallest > self.__data[cursor]:
                    smallest = self.__data[cursor]
                    self.__currentHead = cursor

            return min
        else:
            max = self.__data[self.__currentHead]
            del self.__data[self.__currentHead]

            largest = self.__data[0]
            self.__currentHead = 0

            for cursor in range(len(self.__data) - 1):
                if largest < self.__data[cursor]:
                    largest = self.__data[cursor]
                    self.__currentHead = cursor

            return max

    def __len__(self):
        return len(self.__data)

    def isEmpty(self):
        return len(self.__data) == 0

    def clear(self):
        self.__data = []

    def peekTop(self):
        """
        Runs in constant O(1) time
        :return: object
        """
        if self.isEmpty():
            raise PriorityQueueException("The queue is empty.")

        return self.__data[self.__currentHead]

    def size(self):
        return len(self.__data)

if __name__ == '__main__':
    queue = ArrayUnsortedPriorityQueue(itemType=str)
    a = ['10', '23', '45', '-1', '2', '0', '1', '1', '78','west']

    for i in range(len(a)):
        queue.insert(a[i])

    b = []
    # for i in range(len(queue)):
    #     b.append(queue.removeTop())

    print(queue.peekTop())
    queue.removeTop()

    print(queue.peekTop())
    queue.removeTop()

    print(queue.peekTop())




