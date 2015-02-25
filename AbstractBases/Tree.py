
from abc import ABCMeta, abstractmethod

class Tree (metaclass=ABCMeta):
    """
    Class provide abstract implementation of a general Tree ADT.
    """

    class Position:
        """
        Class represent the position of the node of the tree.
        """
        def element(self):
            """
            Returns the element stored at this position.
            """
            pass

        def node(self):
            """
            Returns the node at this position.
            """
            pass

        def listContainer(self):
            """
            Returns the tree to which this position belongs.
            """
            pass

        def __eq__(self, other):
            """
            Override the equals method to compare position with another one.
            """

        def __ne__(self, other):
            """
            Override the not equals method to compare position with another one.
            """
            return not (self == other)

    @abstractmethod
    def root(self):
        """
        return the position of the root of the tree or None if the tree is empty.
        :return: Position object
        """

    @abstractmethod
    def parent(self, p):
        """
        Returns the parent of a position or None if position is the root.
        :param p: position object in question
        :return: Position
        """

    @abstractmethod
    def children(self, p):
        """
        Yield an iteration of Positions representing p's children or None if it has no children.
        :param p: p in question
        :return: Generator of position
        """

    @abstractmethod
    def numOfChildren(self, p):
        """
        Returns the number of children that Position p has
        :param p: position in question
        :return: integer
        """

    @abstractmethod
    def isEmpty(self):
        """
        Return True if tree is empty.
        :return: Boolean
        """
        return len(self)

    @abstractmethod
    def __len__(self):
        """
        Returns the number of nodes in a tree.
        :return: integer
        """

    @abstractmethod
    def isLeaf(self, p):
        """
        Returns True if Position p is a leaf
        :param p: position in question
        :return: Boolean
        """
        return self.numOfChildren(p) == 0

    @abstractmethod
    def isRoot(self, p):
        """
        Returns True if position is the root of the tree.
        :param p: position in question
        :return: Boolean
        """
        return self.parent(p) is None

    @abstractmethod
    def height(self, p=None):
        """
        Returns the height of the subtree rooted at Position p
        :param p: position in question
        :return: int
        """
        if self.root() is None:
            return 0

        if p is None:
            p = self.root()

        return self.__height(p)

    @abstractmethod
    def __height(self, p):
        """
        Used recursively with height to compute the height of a subtree rooted at position p.
        :param p: position in question.
        :return: int
        """
        if self.isLeaf(p):
            return 0

        return 1 + max(self.__height(child) for child in self.children(p))

    @abstractmethod
    def depth(self, p):
        """
        Returns the number of parent a position has with the position exclusive.
        :param p: position in question
        :return: int
        """
        parent = self.parent(p)

        if parent is None:
            return 0
        else:
            return 1 + self.depth(parent)



