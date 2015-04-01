
from AbstractBases.PositionalList import PositionalListADT as AbstractBaseList
from AppException.PostionalException import PositionalException


class LinkedPositionalList(AbstractBaseList):
    """
    Class implement the positional list ADT via a doubly
    linked list.
    """
    class __Node:
        """
         Class represent a node in the LL
        """
        def __init__(self, e, prevNode, nextNode):
            self.__element = e
            self.__nextNode = nextNode
            self.__prevNode = prevNode

        def nextNode(self, node):
            if node is None:
                return self.__nextNode
            self.__nextNode = node

        def prevNode(self, node):
            if node is None:
                return self.__prevNode
            self.__prevNode = node

        def element(self, e):
            if e is None:
                return self.__element
            self.__element = e

        def dispose(self):
            self.__element = self.__prevNode = self.__nextNode = None

    class __Position:
        """
         Class represent the position of each node in the list
        """
        def __init__(self, node, container):
            self.__node = node
            self.__listContainer = container

        def element(self):
            return self.__node.element()

        def node(self):
            return self.__node

        def listContainer(self):
            return self.__listContainer

        def __eq__(self, other):
            return type(self) is type(other) and self.node() is other.node()

        def __ne__(self, other):
            return not (self == other)

    def __init__(self):
        self.__header = self.__Node(None, None, None)
        self.__trailer = self.__Node(None, None, None)

        self.__header.nextNode(self.__trailer)
        self.__trailer.prevNode(self.__header)

        self.__size = 0

    def __insertBetween(self, e, prevNode, nextNode):
        if not isinstance(prevNode, self.__Node):
            raise PositionalException("The prevNode must be a proper __Node type.")
        if not isinstance(nextNode, self.__Node):
            raise PositionalException("The nextNode must be a proper __Node type.")

        newNode = self.__Node(e, prevNode, nextNode)
        prevNode.nextNode(newNode)
        nextNode.prevNode(newNode)

        return self.__newPosition(newNode)

    def __removeNode(self, node):
        if not isinstance(node, self.__Node):
            raise PositionalException("The node must be a proper __Node type.")

        prevNode = node.prevNode()
        nextNode = node.nextNode()

        prevNode.nextNode(nextNode)
        nextNode.prevNode(prevNode)

        node.dispose()

    def __newPosition(self, node):
        if node is self.__header or node is self.__trailer:
            return None
        return self.__Position(node, self)

    def __validatePosition(self, p):
        if not isinstance(p, self.__Position):
            raise PositionalException("p must be a proper __Position type.")
        if p.listContainer() is not self:
            raise PositionalException("p does not belong to this list.")
        if p.node().nextNode() is None:
            raise PositionalException("p is no more a valid position of the list.")
        return p.node()

    def first(self):
        return self.__newPosition(self.__header.nextNode())

    def last(self):
        return self.__newPosition(self.__trailer.prevNode())

    def after(self, p):
        node = self.__validatePosition(p)
        return self.__newPosition(node.nextNode())

    def before(self, p):
        node = self.__validatePosition(p)
        return self.__newPosition(node.prevNode())

    def remove(self, p):
        node = self.__validatePosition(p)
        self.__removeNode(node)
        self.__size -= 1

    def addLast(self, e):
        position = self.__insertBetween(e, self.__trailer.prevNode(), self.__header)
        self.__size += 1
        return position

    def addFirst(self, e):
        position = self.__insertBetween(e, self.__header, self.__header.nextNode())
        self.__size += 1
        return position

    def addAfter(self, e, p):
        node = self.__validatePosition(p)
        position = self.__insertBetween(e, node, node.nextNode())
        self.__size += 1
        return position

    def addBefore(self, e, p):
        node = self.__validatePosition(p)
        position = self.__insertBetween(e, node.prevNode(), node)
        self.__size += 1
        return position

    def replace(self, e, p):
        node = self.__validatePosition(p)
        node.element(e)

    def isEmpty(self):
        return self.__size == 0

    def __iter__(self):
        cursor = self.first()

        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)