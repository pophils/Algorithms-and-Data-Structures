from AbstractBases.BinaryTree import BinaryTree as AbstractBinaryTree
from AppException.TreeException import TreeException


class ArrayBinaryTree(AbstractBinaryTree):
    """
    Class provides an array based implementation of a binary tree.
    """

    def __init__(self):
        self.__data = []
        self.__size = 0

    def root(self):
        if self.__data[0] is None or len(self.__data) < 1:
            raise TreeException("The tree is empty.")
        return self.__data[0]

    def addRoot(self, e):
        if self.__data[0] is not None or len(self.__data) > 0:
            raise TreeException("The tree already has a root.")

        self.__data[0] = e

    def numOfChildren(self, i):
        """
        Returns the number of children of a node at index i
        :param i: position index
        """
        if not self.__isValidLevelNumber(i):
            raise IndexError("Index is not a valid position.")
        count = 0

        if self.__hasLeft(i):
            count = 1
        if self.__hasRight(i):
            count += 1

        return count

    def __hasLeft(self, i):
        return (i * 2) + 1 < len(self.__data)

    def __hasRight(self, i):
        return (i * 2) + 2 < len(self.__data)

    def __isValidLevelNumber(self, i):
        return i < len(self.__data)

    def left(self, i):
        if not self.__isValidLevelNumber(i):
            raise IndexError("Index is not a valid position.")

        if not self.__hasLeft(i):
            raise TreeException("Position has no left child")

        return (i*2) + 1

    def right(self, i):
        if not self.__isValidLevelNumber(i):
            raise IndexError("Index is not a valid position.")

        if not self.__hasRight(i):
            raise TreeException("Position has no right child")

        return (i*2) + 2

    def parent(self, i):
        if not self.__isValidLevelNumber(i):
            raise IndexError("Index is not a valid position.")
        return (i - 1) / 2

    def __len__(self):
        return len(self.__data)

    def positions(self):
        pass

    def elements(self):
        pass

    def breadthFirst(self):
        pass

    def postOrder(self):
        pass

    def preOrder(self):
        pass

    def inOrder(self):
        pass