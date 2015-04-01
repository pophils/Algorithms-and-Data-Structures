from AbstractBases.BinaryTree import BinaryTree as AbstractBinaryTree
from AppException.TreeException import TreeException


class ArrayBinaryTree(AbstractBinaryTree):
    """
    Class provides an array based implementation of a binary tree.
    Mostly tree are reference based. Using an array based implementation
    will be efficient in space complexity if the problem size is known
    in advance or in a context that requires a complete binary tree.
    Otherwise, it could lead to a sparse tree with several spaces in the
    underlying left empty.
    """

    def __init__(self, defaultCapacity=20):

        if defaultCapacity is not None and not isinstance(defaultCapacity, int):
            raise TypeError("The defaultCapacity must be an integer.")
        self.__DefaultCapacity = defaultCapacity

        self.__data = [None] * self.__DefaultCapacity
        self.__size = 0

    def root(self):
        if self.__data[0] is None:
            raise TreeException("The tree is empty.")
        return 0

    def addRoot(self, e):
        if self.__data[0] is not None:
            raise TreeException("The tree already has a root.")

        self.__data[0] = e
        self.__size = 1

        return 0

    def addLeft(self, i, e):

        self.__ValidateLevelNumber(i)

        if self.__hasLeft(i):
            raise TreeException("This position already has a left child.")

        newPosition = (i*2) + 1

        if newPosition > len(self.__data):
            self.__resize(2*len(self.__data))

        self.__data[newPosition] = e

        self.__size += 1

        return newPosition

    def addRight(self, i, e):

        self.__ValidateLevelNumber(i)

        if self.__hasRight(i):
            raise TreeException("This position already has a right child.")

        newPosition = (i*2) + 2

        if newPosition > len(self.__data):
            self.__resize(2*len(self.__data))

        self.__data[newPosition] = e

        self.__size += 1

        return newPosition

    def numOfChildren(self, i):
        """
        Returns the number of children of a node at index i
        :param i: position index
        """
        self.__ValidateLevelNumber(i)
        count = 0

        if self.__hasLeft(i):
            count = 1
        if self.__hasRight(i):
            count += 1

        return count

    def element(self, i):
        """
        Returns the number of children of a node at index i
        :param i: position index
        """
        self.__ValidateLevelNumber(i)

        return self.__data[i]

    def left(self, i):
        self.__ValidateLevelNumber(i)

        if not self.__hasLeft(i):
            return None

        return (i*2) + 1

    def right(self, i):
        self.__ValidateLevelNumber(i)

        if not self.__hasRight(i):
            return None

        return (i*2) + 2

    def parent(self, i):
        self.__ValidateLevelNumber(i)
        return (i - 1) // 2

    def isRoot(self, i):
        """
        Returns True if position is the root of the tree.
        :param i: level number
        :return: Boolean
        """
        return i == 0

    def children(self, i):
        self.__ValidateLevelNumber(i)

        if self.__hasLeft(i):
            yield self.left(i)

        if self.__hasRight(i):
            yield self.right(i)

    def isEmpty(self):
        return self.__size == 0

    def preOrder(self):
        if self.isEmpty():
            return None
        for pos in self.__preOrder(self.root()):
            yield pos

    def postOrder(self):
        if self.isEmpty():
            return None
        for pos in self.__postOrder(self.root()):
            yield pos

    def inOrder(self):
        if self.isEmpty():
            return None
        for pos in self.__inOrder(self.root()):
            yield pos

    def breadthFirst(self):
        if not self.isEmpty():
            yield self.root()

            yieldCount = 1
            cursor = 1

            while yieldCount < self.__size:
                if self.__data[cursor] is not None:
                    yield cursor
                    yieldCount += 1
                cursor += 1

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
            yield self.__data[pos]

    def replace(self, i, e):
        self.__ValidateLevelNumber(i)

        self.__data[i] = e

    def dispose(self):
        self.__data = [None]*self.__DefaultCapacity
        self.__size = 0

    def attach(self, i, t1):
        """
        Attach a tree to at index i. It is implemented recursively via a customized pre-order
        traversal through the tree.
        :param i: level numbering
        :param t1: Tree to be attached
        :exception raise a TreeException if position is not a leaf.
        """

        if not isinstance(t1, ArrayBinaryTree):
            raise TreeException("The tree types are not the same.")

        if not type(self) is type(t1):
            raise TreeException("The tree types are not the same.")

        if not self.isLeaf(i):
            raise TreeException("The index is not a Leaf.")

        # No need to call validatePosition, cos this would have been done when testing if it is leaf
        self.__attachPreOrder(t1, i, t1.root())

        t1.dispose()

    def depth(self, i):
        pass

    def delete(self):
        pass

    def __attachPreOrder(self, tree, currentParentIndex, i):

        if tree.isRoot(i):
            if self.__hasLeft(currentParentIndex):
                currentParentIndex = self.addRight(currentParentIndex, tree.element(i))
            else:
                currentParentIndex = self.addLeft(currentParentIndex, tree.element(i))
        else:
            parent = tree.parent(i)
            if tree.right(parent) == i:
                currentParentIndex = self.addRight(currentParentIndex, tree.element(i))
            else:
                currentParentIndex = self.addLeft(currentParentIndex, tree.element(i))

        for child in tree.children(i):
            self.__attachPreOrder(tree, currentParentIndex, child)

    def __postOrder(self, i):
        for child in self.children(i):
            for pos in self.__postOrder(child):
                yield pos
        yield i

    def __preOrder(self, i):
        yield i
        for child in self.children(i):
            for pos in self.__preOrder(child):
                yield pos

    def __inOrder(self, i):

        leftChild = self.left(i)
        rightChild = self.right(i)

        if leftChild is not None:
            for pos in self.__inOrder(leftChild):
                yield pos

        yield i

        if rightChild is not None:
            for pos in self.__inOrder(rightChild):
                yield pos

    def __len__(self):
        return self.__size

    def __resize(self, newLen):

        tempBuffer = [None] * newLen

        for cursor in range(len(self.__data)):
            tempBuffer[cursor] = self.__data[cursor]

        self.__data = tempBuffer

    def __isLeaf(self, i):
        return self.numOfChildren(i) == 0

    def __hasLeft(self, i):
        return (i * 2) + 1 < len(self.__data) and self.__data[(i * 2) + 1] is not None

    def __hasRight(self, i):
        return (i * 2) + 2 < len(self.__data) and self.__data[(i * 2) + 2] is not None

    def __ValidateLevelNumber(self, i):
        if i >= len(self.__data):
            raise IndexError("Index is not a valid level number.")


if __name__ == '__main__':
    t = ArrayBinaryTree()

    rootPosition = t.addRoot('root')

    l1 = t.addLeft(rootPosition, 'left child')
    r1 = t.addRight(rootPosition, 'right child')

    l2 = t.addLeft(l1, 'left child2')
    r2 = t.addRight(r1, 'right child2')

    r3 = t.addRight(r2, 'right child3')
    l3 = t.addLeft(r2, 'left child3')

    r4 = t.addRight(l3, 'right child4')
    l4 = t.addLeft(l3, 'left child4')

    print("All t elements via post-order traversal after attaching t1")
    for s in t.positions(1):
        print("\t", t.element(s))

    print("####################################################")

    print("All t elements via breadth-first traversal")
    for s in t.positions(2):
        print("\t", t.element(s))

    print("####################################################")
    print("####################################################")

    t2 = ArrayBinaryTree()

    rootPosition = t2.addRoot('root')

    l1 = t2.addLeft(rootPosition, 'left child')
    r1 = t2.addRight(rootPosition, 'right child')

    l2 = t2.addLeft(l1, 'left child2')
    r2 = t2.addRight(r1, 'right child2')

    r3 = t2.addRight(r2, 'right child3')
    l3 = t2.addLeft(r2, 'left child3')

    r4 = t2.addRight(l3, 'right child4')
    l41 = t2.addLeft(l3, 'left child4')

    print("length of tree before merging: %s" % len(t))
    t.attach(l4, t2)

    print("All t elements via post-order traversal after attaching t1")
    for s in t.positions(1):
        print("\t", t.element(s))

    print("####################################################")

    print("All t elements via breadth-first traversal after attaching t1")
    for s in t.positions(2):
        print("\t", t.element(s))

    print("length of tree after merging: %s" % len(t))