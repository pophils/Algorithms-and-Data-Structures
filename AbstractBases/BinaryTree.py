
from abc import ABCMeta, abstractmethod
from AbstractBases.Tree import Tree


class BinaryTree (metaclass=ABCMeta, Tree):
    """
    Class provide abstract implementation of a binary Tree ADT.
    """

    @abstractmethod
    def left(self, p):
        """
        Return left child of a given position p or None if p has no left child.
        :param :p position in question
        :return: Position object
        """
    @abstractmethod
    def right(self, p):
        """
        Return right child of a given position p or None if p has no right child.
        :param :p position in question
        :return: Position object
        """

    def sibling(self, p):
        """
        Return the left or right sibling of a position.
        :param :p position in question
        :return: Position object
        """
        parent = self.parent(p)

        if parent is None:
            return None

        if self.left(parent) == p:
            return self.right(parent)
        return self.left(parent)

    def children(self, p):
        """
        Yield an iteration of Positions representing p's children or None if it has no children.
        :param p: p in question
        :return: Generator of position
        """
        leftChild = self.left(p)
        rightChild = self.right(p)

        if leftChild is not None:
            yield leftChild
        if rightChild is not None:
            yield rightChild

