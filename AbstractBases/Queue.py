
from abc import ABCMeta, abstractmethod


class Queue (metaclass=ABCMeta):

    @abstractmethod
    def enqueue(self, e):
        """
         Push an item to the Queue.
        """

    @abstractmethod
    def dequeue(self):
        """
        Remove and return the first item of the queue.
        :return: Object
        :exception: Raises a QueueException if the queue is empty.
        """

    @abstractmethod
    def top(self):
        """
        Returns the first element in the queue.
        :return: Object
        :exception: Raises a StackException if the queue is empty.
        """

    @abstractmethod
    def size(self):
        """
         Return the size of the queue.
        :return: int
        """

    @abstractmethod
    def isEmpty(self):
        """
        Checks if the queue is empty.
        :return: boolean
        """

    @abstractmethod
    def transfer(self, t=None):
        """
         R-6.3 Transfer the element of this queue to a new queue.
        :param t: Destination Queue
        :return: The destination queue
        """

    @abstractmethod
    def clear(self):
        """
        Clears all the element of the queue.
        """

    @abstractmethod
    def toList(self):
        """
        Convert queue to a an array List.
        :return: list
        """

    @abstractmethod
    def __iter__(self):
        """
        An iterator for over the element of the queue.
        """

    @abstractmethod
    def __len__(self):
        """
        Returns the len of the Queue
        """