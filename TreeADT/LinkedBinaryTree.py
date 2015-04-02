from AbstractBases.BinaryTree import BinaryTree
from AppException.TreeException import TreeException
from ArrayListADT.ArrayQueue import ArrayQueue


class LinkedBinaryTree(BinaryTree):
    """
    Class provides a Linked implementation of the Binary Tree.
    All methods runs in constant time except for the depth(O(D+1)) where d is the
    depth of the position and height that runs in O(n) time where n is the number of descendant
    of position p..
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

        def parent(self, node=None):
            if node is None:
                return self.__parent
            else:
                self.__parent = node

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
            self.parent(self)

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

    def newPosition(self, node):
        """
        Returns a new Position
        :param node: node having the position
        :return:
        """
        return self.Position(node, self) if node is not None else None

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
        if p.node().parent() is p.node():
            raise ValueError("P is no longer valid")
        # if p.node().parent() is None and p != self.root():
        #     raise TreeException("P is no more valid.")

        return p.node()

    def __init__(self):
        self.__root = None
        self.__size = 0

    def root(self):
        return self.newPosition(self.__root)

    def addRoot(self, e):
        """
        Create a root Node
        :param e: item to be stored at the root.
        :return: Position of the root.
        :exception raise a TreeException if tree already has a root element.
        """
        if self.__root is not None:
            raise TreeException("The tree already has a root.")

        self.__root = self._Node(e)
        self.__size = 1

        return self.newPosition(self.__root)

    def parent(self, p):
        node = self.validatePosition(p)
        return self.newPosition(node.parent())

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

        return self.newPosition(node.right())

    def left(self, p):
        """
        returns the position of Position p right child.
        :param p: Position P
        :return: Position
        """
        node = self.validatePosition(p)
        return self.newPosition(node.left())

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

        newNode = self._Node(e, node)
        node.right(newNode)
        # node.right(self._Node(e, node))
        self.__size += 1
        return self.newPosition(node.right())

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

        # node.left(self._Node(e, node))
        newNode = self._Node(e, node)
        node.left(newNode)
        self.__size += 1
        return self.newPosition(node.left())

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

    def clear(self):
        self.__root = None
        self.__size = 0

    def attach(self, p, t1):
        """
        Attach two subtrees at position p
        :param p: Position p
        :param t1: Tree to be attached
        :exception raise a TreeException if position is not a leaf.
        """

        if not type(self) is type(t1):
            raise TypeError("The tree types are not the same.")

        node = self.validatePosition(p)

        if node.right() is not None or node.left() is not None:
            raise TreeException("The position,p is not a leaf.")

        t1Len = len(t1)
        self.__size += t1Len

        if t1Len > 0:
            t1.root().node().parent(node)
            node.left(t1.root().node())
            t1.clear()

    def postOrder(self):
        """
        Runs recursively in O(n) time. A single recursive call will be
        made on each position.
        """
        if not self.isEmpty():
            for pos in self._PostOrderTraversal(self.root()):
                yield pos

    def _PostOrderTraversal(self, p):

        for child in self.children(p):
            for pos in self._PostOrderTraversal(child):
                yield pos

        yield p

    def preOrder(self):
        """
        Runs recursively in O(n) time. A single recursive call will be
        made on each position. It is assumed that the action takes O(1) time
        """
        if not self.isEmpty():
            for pos in self._PreOrderTraversal(self.root()):
                yield pos

    def _PreOrderTraversal(self, p):
        yield p
        for child in self.children(p):
            for pos in self._PreOrderTraversal(child):
                yield pos

    def breadthFirst(self):
        """
        Runs non-recursively in O(n) time. It used
        a queue internally. A total 2n call to both enqueue and dequeue is
        made.
        """
        if not self.isEmpty():
            queue = ArrayQueue()
            queue.enqueue(self.root())

            while not queue.isEmpty():
                p = queue.dequeue()
                yield p
                for child in self.children(p):
                    queue.enqueue(child)

    def inOrder(self):

        if not self.isEmpty():
            for pos in self._InOrderTraversal(self.root()):
                yield pos

    def _InOrderTraversal(self, p):

        leftChild = self.left(p)
        rightChild = self.right(p)

        if leftChild is not None:
            for pos in self._InOrderTraversal(leftChild):
                yield pos

        yield p

        if rightChild is not None:
            for pos in self._InOrderTraversal(rightChild):
                yield pos

    def elements(self, traversal=0):
        """
        Generates an iteration of all elements stored in the tree. The default traversal is pre-order.
        Traversal options:
            pre-order: 0
            post-order: 1
            bread-first: 2
            in-order: 3
        :return: Generator object
        """
        for pos in self.positions(traversal):
            yield pos.element()

    def positions(self, traversal=0):
        """
        Generates the positions of a tree. The default traversal is pre-order.
        Traversal options:
            pre-order: 0
            post-order: 1
            bread-first: 2
            in-order: 3
        :param: Traversal choice of the tree
        """
        if traversal == 0:
            return self.preOrder()
        elif traversal == 1:
            return self.postOrder()
        elif traversal == 2:
            return self.breadthFirst()
        elif traversal == 3:
            return self.inOrder()
        else:
            return self.preOrder()


if __name__ == '__main__':
    t = LinkedBinaryTree()

    rootPosition = t.addRoot('root')

    l1 = t.addLeft(rootPosition, 'left child')
    r1 = t.addRight(rootPosition, 'right child')

    l2 = t.addLeft(l1, 'left child2')
    r2 = t.addRight(r1, 'right child2')

    r3 = t.addRight(r2, 'right child3')
    l3 = t.addLeft(r2, 'left child3')

    r4 = t.addRight(l3, 'right child4')
    l4 = t.addLeft(l3, 'left child4')

    print("All t elements via post-order traversal")
    for s in t.positions(1):
        print("\t", s.element())

    print("##########################")

    print("All t elements via breadth-first traversal")
    for s in t.positions(2):
        print("\t", s.element())

    print("####################################################")
    print("####################################################")

    t2 = LinkedBinaryTree()

    rootPosition = t2.addRoot('root')

    l1 = t2.addLeft(rootPosition, 'left child')
    r1 = t2.addRight(rootPosition, 'right child')

    l2 = t2.addLeft(l1, 'left child2')
    r2 = t2.addRight(r1, 'right child2')

    r3 = t2.addRight(r2, 'right child3')
    l3 = t2.addLeft(r2, 'left child3')

    r4 = t2.addRight(l3, 'right child4')
    l41 = t2.addLeft(l3, 'left child4')

    t.attach(l4, t2)

    print("All t elements via post-order traversal after attaching t1")
    for s in t.positions(1):
        print("\t", s.element())

    print("##########################")

    print("All t elements via breadth-first traversal after attaching t1")
    for s in t.positions(2):
        print("\t", s.element())

    # print("Root Children")
    # for s in t.children(rootPosition):
    #     print("\t", s.element())
    #
    # print("##########################")
    #
    # print("R2 Children")
    # for s in t.children(r2):
    #     print("\t", s.element())
    #
    # print("##########################")
    #
    # print("All elements via pre-order traversal")
    # for s in t.positions():
    #     print("\t", s.element())
    #
    # print("##########################")
    #
    # print("All elements via post-order traversal")
    # for s in t.positions(1):
    #     print("\t", s.element())
    #
    # print("##########################")
    #
    # print("All elements via breadth-first traversal")
    # for s in t.positions(2):
    #     print("\t", s.element())
    #
    # print("##########################")
    #
    # print("All elements via in-order traversal")
    # for s in t.positions(3):
    #     print("\t", s.element())
    #
    # print("##########################")
    #
    # print("Height of tree")
    # print(t.height())
    #
    # print("##########################")
    #
    # print("Depth of position R2")
    # print(t.depth(r2))
    #
    # print("##########################")
    #
    # print("Depth of tree positions")
    # depthList = [t.depth(d) for d in t.positions()]
    #
    # print(depthList)




