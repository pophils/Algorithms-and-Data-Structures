from AbstractBases.BinaryTree import BinaryTree
from AppException.TreeException import TreeException


class LinkedBinaryTree(BinaryTree):
    """
    Class gives an Linked implementation of the Binary Tree.
    """

    class _Node:

        def __init__(self, e, parent=None, left=None, right=None):
            self.__element = e
            self.__parent = parent
            self.__left = left
            self.__right = right

        def element(self, e=None):
            if e is None:
                return self.__element
            else:
                self.__element = e

        def parent(self):
            return self.__parent

        def right(self, node=None):
            if node is None:
                return self.__right
            else:
                self.__right = node

        def left(self, node=None):
            if node is None:
                return self.__left
            else:
                self.__left = node

        def __dispose(self):
            self.__element = self.__parent = self.__left = self.__right = None

    class Position(BinaryTree.Position):

        def __init__(self, node, tree):
            self.__node = node
            self.__tree = tree

        def element(self):
            return self.__node.element()

        def node(self):
            return self.__node

        def tree(self):
            return self.__tree

        def __eq__(self, other):
            return type(self) is type(other) and self.node() is other.node()

    def newPosition(self, node, tree):
        """
        Returns a new Position
        :param node: node having the position
        :param tree: tree to which the position belongs
        :return:
        """
        return self.Position(node, tree)

    def validatePosition(self, p):
        """
        Returns a Node Object if the Position, p is valid
        :param p: Position P
        :return: Node Object
        """
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper Position type.")
        if p.tree() is not self:
            raise ValueError("p does not belong to this tree.")
        if p.node().parent() is None and p is not self.root():
            raise TreeException("P is no more valid.")

        return p.node()

    def __init__(self):
        self.__root = None
        self.__size = 0

    def root(self):
        return self.newPosition(self.__root, self)

    def addRoot(self, e):
        """
        Create a root Node
        :param e: item to be stored at the root.
        :return: Position of the root.
        :exception raise a TreeException if tree already has a root element.
        """
        if self.root() is not None:
            raise TreeException("The tree already has a root.")

        self.__root = self._Node(e)
        self.__size = 1

        return self.newPosition(self.__root)

    def parent(self, p):
        node = self.validatePosition(p)
        return self.newPosition(node.parent(), self)

    def numOfChildren(self, p):
        node = self.validatePosition(p)

        count = 0

        if node.left() is not None:
            count += 1
        if node.right() is not None:
            count += 1

        return count

    def right(self, p):
        """
        returns the position of Position p right child.
        :param p: Position P
        :return: Position
        """
        node = self.validatePosition(p)
        return node.right()

    def left(self, p):
        """
        returns the position of Position p right child.
        :param p: Position P
        :return: Position
        """
        node = self.validatePosition(p)
        return node.left()

    def __len__(self):
        return self.__size

    def addRight(self, p, e):
        """
        Add a right child to a position p.
        :param p: Parent Position
        :param e: Item to be stored
        :return: Position
        :exception raise a ValueError if p already has a right child
        """
        node = self.validatePosition(p)

        if node.right() is not None:
            raise ValueError("This position already has a right child")

        self.__size += 1
        return self.newPosition(node.right(self._Node(e, node)))

    def addLeft(self, p, e):
        """
        Add a left child to a position p.
        :param p: Parent Position
        :param e: Item to be stored
        :return: Position
        :exception raise a ValueError if p already has a left child
        """
        node = self.validatePosition(p)

        if node.left() is not None:
            raise ValueError("This position already has a left child")

        self.__size += 1
        return self.newPosition(node.left(self._Node(e, node)))

    def replace(self, p, e):
        """
        Replace the item stored at a Position p
        :param p: position of the node
        :param e: new item
        """
        node = self.validatePosition(p)
        node.element(e)

    def delete(self, p):
        """
        Delete a position from the tree.
        :param p: Position to be deleted
        :exception raise a TreeException if p has more than 1 child.
        """
        node = self.validatePosition(p)

        if self.numOfChildren(p) > 1:
            raise TreeException("This node cannot be deleted as it has more than 1 child")

        child = node.left() if node.left() is not None else node.right()

        if child is not None:
            child.parent(node.parent())

        if node is self.__root:
            self.__root = child
        else:
            parent = node.parent()
            if parent.left() is node:
                parent.left(child)
            else:
                parent.right(child)

        self.__size -= 1

        node.__dispose()

    def dispose(self):
        self.__root = None
        self.__size = 0

    def attach(self, p, t1, t2):
        """
        Attach two subtrees at position p
        :param p: Position p
        :param t1: Tree 1
        :param t2: Tree 2
        :exception raise a TreeException if position is not a leaf.
        """
        node = self.validatePosition(p)

        if node.right() is None or node.left() is None:
            raise TreeException("The position,p is not a leaf.")
        if not type(self) is type(t1) is type(t2):
            raise TreeException("The tree types are not the same.")

        t1Len = len(t1)
        t2Len = len(t2)

        self.__size += t1Len + t2Len

        if t1Len > 0:
            t1.root().node().parent(node)
            node.left(t1.root().node())
            t1.dispose()

        if t2Len > 0:
            t2.root().node().parent(node)
            node.right(t2.root().node())
            t2.dispose()