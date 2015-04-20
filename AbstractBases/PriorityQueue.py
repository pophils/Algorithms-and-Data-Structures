
from abc import ABCMeta, abstractmethod


class PriorityQueue (metaclass=ABCMeta):

    @abstractmethod
    def insert(self, e):
        """
         Add an item to the Queue.
         :param e: item to be added must be comparable
        """

    @abstractmethod
    def peekTop(self):
        """
        Return the first item of the queue
        """

    @abstractmethod
    def removeTop(self):
        """
        Remove and returns the first item of the Queue.
        """

    @abstractmethod
    def __len__(self):
        """
        Return the size of the queue
        :return: int
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
    def clear(self):
        """
        Clears all the element of the deque.
        """