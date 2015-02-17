
from abc import ABCMeta, abstractmethod


class Stack (metaclass=ABCMeta):

    @abstractmethod
    def push(self):
        """
         Push an item to the stack.
        """

    @abstractmethod
    def pop(self):
        """
        Remove and return the last item of the stack.
        :return: Object
        :exception: Raises a StackException if stack is empty.
        """

    @abstractmethod
    def top(self):
        """
        Returns the first element in the stack.
        :return: Object
        :exception: Raises a StackException if stack is empty.
        """

    @abstractmethod
    def size(self):
        """
         Return the size of the stack.
        :return: int
        """

    @abstractmethod
    def isEmpty(self):
        """
        Checks if the stack is empty.
        :return: boolean
        """

    @abstractmethod
    def clear(self):
        """
        Clears all the element of the stack.
        :return: boolean
        """

    @abstractmethod
    def transfer(self, t=None):
        """
         R-6.3 Transfer the element of this stack to a destination stack.
        :param t: Destination Stack
        :return: The destination stack
        """

    @abstractmethod
    def toList(self):
        """
        Convert stack to a an array List.
        :return: list
        """

    @abstractmethod
    def __iter__(self):
        """
        An iterator for the stack
        """
