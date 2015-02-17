
from abc import ABCMeta, abstractmethod


class PositionalListADT (metaclass=ABCMeta):

    @abstractmethod
    def first(self):
        """
        Returns the position of the first item.
        :return: position object
        """

    @abstractmethod
    def last(self):
        """
        Returns the position of the last item.
        :return: position object
        """

    @abstractmethod
    def before(self, p):
        """
        Returns the position immediately before position, p.
        :return: position object
        """

    @abstractmethod
    def after(self, p):
        """
        Returns the position immediately after position, p.
        :return: position object
        """

    @abstractmethod
    def isEmpty(self):
        """
        Checks if the list is empty.
        :return: boolean
        """

    @abstractmethod
    def addFirst(self, e):
        """
        Add an item to the beginning of the list.
        :param e: item to be added.
        """

    @abstractmethod
    def addLast(self, e):
        """
        Add an item to the end of the list.
        :param e: item to be added.
        """

    @abstractmethod
    def addBefore(self, e, p):
        """
        Add an item before a position, p
        :param e: item to be added.
        :param p: Position p.
        """

    @abstractmethod
    def addAfter(self, e, p):
        """
        Add an item after a position, p
        :param e: item to be added.
        :param p: Position p.
        """

    @abstractmethod
    def replace(self, e, p):
        """
        Replace an item at a position, p with an item e
        :param e: item to be replaced with.
        :param p: Position of the item to be replaced.
        """

    @abstractmethod
    def remove(self, p):
        """
        Remove and return an item from the list at a particular position p
        :param p: Position of the element
        :return: object
        """

    @abstractmethod
    def clear(self):
        """
        Clears all the element of the list.
        """

    @abstractmethod
    def __iter__(self):
        """
        An iterator for over the element of the List.
        """