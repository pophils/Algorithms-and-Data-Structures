
from abc import ABCMeta, abstractmethod


class Deque (metaclass=ABCMeta):

    @abstractmethod
    def append(self, e):
        """
         Add an item to the Deque.
         :param e: item to be added
        """

    @abstractmethod
    def appendLeft(self, e):
        """
        Add an item to the front of the Deque
        :param e: item to be added
        """

    @abstractmethod
    def pop(self):
        """
        Remove and returns the last item of the Deque.
        :return: Object
        :exception: Raises a DequeException if the deque is empty.
        """

    @abstractmethod
    def popLeft(self):
        """
        Remove and returns the first item of the Deque.
        :return: Object
        :exception: Raises a DequeException if the deque is empty.
        """

    @abstractmethod
    def size(self):
        """
         Return the size of the deque.
        :return: int
        """

    @abstractmethod
    def isEmpty(self):
        """
        Checks if the deque is empty.
        :return: boolean
        """

    @abstractmethod
    def clear(self):
        """
        Clears all the element of the deque.
        """

    @abstractmethod
    def toList(self):
        """
        Convert deque to a an array List.
        :return: list
        """

    @abstractmethod
    def __iter__(self):
        """
        An iterator for over the element of the deque.
        """

    @abstractmethod
    def __len__(self):
        """
        Returns the len of the Deque
        """

    @abstractmethod
    def rotate(self, k):
        """
        Rotates the element of the deque by a constant K
        :param k: item to be added
        """