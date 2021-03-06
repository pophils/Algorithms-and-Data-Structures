
from ArrayListADT.ArrayStack import ArrayStack
from ArrayListADT.ArrayQueue import ArrayQueue
from AppException.ExercisesException import ExercisesException


class Exercises():
    """
    Solutions to exercises of chapter 6 (Stacks and queues).
    """
    @staticmethod
    def __newStack(capacity=None):
        """
        Creates a new stack
        """
        return ArrayStack(capacity)

    @staticmethod
    def transferStack():
        """
        R-6.3 Function transfers element of one stack to another.
        """
        s = Exercises.__newStack(10)
        s.push(10)
        s.push(200)
        s.push('C++')
        s.push('Google Brain')
        s.push('One-time pad')
        s.push(1000)
        s.push('Trampolining')

        print("Stack s1 size: %s" % s.size())
        destStack = s.transfer()

        print("Stack s1 size: %s" % s.size())
        print("Stack destStack size: %s" % destStack.size())

    def emptyStackRecursively(self, s):
        """
        R-6.4 Function recursively remove all elements from a stack.
        """
        if s is None:
            raise ExercisesException("Stack is not defined")

        if len(s) > 0:
            s.pop()
            self.emptyStackRecursively(s)

    @staticmethod
    def reverseList(seq):

        """
        R-6.5: Function use a stack in reversing the element of a list.
               Function's complexity is O(n) i.e running time grows proportionally
               with 2n
               :param seq: List whose element is to be reversed.
        """
        if seq is None:
            raise ExercisesException("The list argument is undefined.")
        if not isinstance(seq, list):
            raise ExercisesException("The sequence is not a list instance.")

        seqLen = len(seq)
        if seqLen > 1:
            tempStack = ArrayStack(seqLen)
            for item in seq:
                tempStack.push(item)
            for index in range(seqLen):
                seq[index] = tempStack.pop()
        return seq

    @staticmethod
    def creativityQ1(r, s, t):
        """
        C-6.23: Given three non-empty stacks R, S,and T, Function provides sequence of operation
                that results in S storing all elements originally in T below all of S’s original
                elements, with both sets of those elements in their original order.
                The final configuration for R should be the same as its original configuration.
                For example, if R =[1,2,3], S =[4,5],and T =[6,7,8,9], the final configuration should
                have R =[1,2,3] and S =[6,7,8,9,4,5].
        :return: tuple of r,s,t
        """

        if not isinstance(r, ArrayStack):
            raise ExercisesException("r is not a Stack type")
        if not isinstance(s, ArrayStack):
            raise ExercisesException("s is not a Stack type")
        if not isinstance(t, ArrayStack):
            raise ExercisesException("t is not a Stack type")

        if not t.isEmpty():
            tLen = t.size()
            r = t.transfer(r)
            while tLen > 0:
                s.push(r.pop())
                tLen -= 1

    @staticmethod
    def creativityQ2(s, item):
        """
        C-6.27: Function searches S for an item x using a queue.
        :param: s: the stack to be searched.
        :param: item: the element to be searched.
        """

        if not isinstance(s, ArrayStack):
            raise ExercisesException("s is not a Stack type")

        stackLen = len(s)
        found = False

        if stackLen > 1:
            tempItem = None
            queue = ArrayQueue(stackLen)
            for i in range(stackLen):
                tempItem = s.pop()
                if item == tempItem:
                    found = True
                    break

                queue.enqueue(tempItem)
                for j in range(len(queue)-1):
                    tempItem = queue.dequeue()
                    queue.enqueue(tempItem)

            if found:
                s.push(tempItem)

            queueLen = len(queue)
            if queueLen > 0:
                while queueLen > 0:
                    s.push(queue.dequeue())
                    queueLen -= 1

        if stackLen == 1:
            if s.top() == item:
                return True

        return found


class QueuedStack():
    """
    C-6.24: Class implement a Stack ADT using a single Queue as an
    instance variable and only a constant memory within the
    method bodies
    """

    def __init__(self, queue=None, capacity=10):

        if queue is None:
            self.__queue = ArrayQueue(capacity)
        else:
            if not isinstance(queue, ArrayQueue):
                raise ExercisesException("The queue is not a Queue type")
            self.__queue = queue

    def push(self, item):
        """
        Push an item to the stack.
        Time complexity is O(1) and O(n) at worst case where n is the current size of the
        underlying queue before pushing a new item.
        :param item: item to be pushed into the stack.
        """
        if len(self.__queue) < 1:
            self.__queue.enqueue(item)
        else:
            # currentLen = len(self.__queue)
            self.__queue.enqueue(item)
            for index in range(len(self.__queue)-1):
                tempItem = self.__queue.dequeue()
                self.__queue.enqueue(tempItem)
                # currentLen -= 1

    def pop(self):
        """
        Pop an item from the stack
        Function runs in constant time O(1)and occasionally at O(n) worst case when
        the underlying queue size needs to be reduced.
        :return: object
        """
        if self.isEmpty():
            raise ExercisesException("The stack is empty.")
        return self.__queue.dequeue()

    def top(self):
        """
        Function returns the first element of the stack.
        it runs in constant O(1) time complexity.
        :return: object
        """
        if self.isEmpty():
            raise ExercisesException("The stack is empty.")
        return self.__queue.top()

    def size(self):
        """
        Function returns the size of the stack.
        Runs in constant O(1) time complexity.
        :return: int
        """
        return len(self.__queue)

    def isEmpty(self):
        """
        Function checks if the stack is empty.
        Runs in constant time O(1) complexity.
        :return: boolean
        """
        return self.__queue.isEmpty()


from AbstractBases.Deque import Deque as AbstractBaseDeque
from AppException.DequeException import DequeException


class StackedDeque(AbstractBaseDeque):
    """
    C-6.26: Class implement a Double-ended Queue ADT using two
    Stacks as an instance variable
    """

    def __init__(self):
        self.__mainStack = ArrayStack()
        self.__tempStack = ArrayStack()
        self.__size = 0

    def append(self, e):
        """
        Runs in amortized O(1) time. Occasionally O(n) times if there is a resizing.
        :param e: Item to be appended
        """
        self.__mainStack.push(e)
        self.__size += 1

    def appendLeft(self, e):
        """
        This will take O(2n) worst case time where n is the current size of the queue
        :param e: item to be appended
        """
        for index in range(self.__size):
            self.__tempStack.push(self.__mainStack.pop())

        self.__mainStack.push(e)
        for index in range(self.__size):
            self.__mainStack.push(self.__tempStack.pop())

        self.__size += 1

    def pop(self):
        """
        Runs in constant O(1) time.
        :return: Object
        """
        self.__size -= 1
        return self.__mainStack.pop()

    def popLeft(self):
        """
        This will take O(2n) worst case time where n is the current size of the queue
        :return: object
        """
        for index in range(self.__size - 1):
            self.__tempStack.push(self.__mainStack.pop())

        e = self.__mainStack.pop()
        self.__size -= 1

        for index in range(self.__size):
            self.__mainStack.push(self.__tempStack.pop())

        return e

    def clear(self):
        self.__mainStack.clear()
        self.__size = 0

    def rotate(self, k):
        """
        Runs in O(2kn) worst case time.
        :param k:
        """
        if not isinstance(k, int):
            raise TypeError("k must be an integer.")

        if self.isEmpty():
            raise DequeException("Deque is empty.")

        for index in range(k):
            currentFirst = self.__mainStack.pop()
            for cursor in range(self.__size - 1):
                self.__tempStack.push(self.__mainStack.pop())
            self.__mainStack.push(currentFirst)
            for cursor in range(self.__size - 1):
                self.__mainStack.push(self.__tempStack.pop())

    def size(self):
        return self.__size

    def toList(self):
        return self.__mainStack.toList()

    def __iter__(self):
        pass

    def __len__(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0


if __name__ == '__main__':
    s1 = StackedDeque()

    s1.append(3)
    s1.append(20)
    s1.append(200)

    print("Stack size: %s" % len(s1))
    print(s1.toList())

    s1.appendLeft(30)
    s1.appendLeft([1, 3, 5, 7, 'google'])

    print("Stack size: %s" % len(s1))
    print(s1.toList())

    s1.pop()

    print("Stack size: %s" % len(s1))
    print(s1.toList())

    s1.appendLeft(111111)
    s1.append(11111111)
    s1.append((12, 13, 24, 'kmeans'))

    print("Stack size: %s" % len(s1))
    print(s1.toList())

    s1.append(False)

    print("Stack size: %s" % len(s1))
    print(s1.toList())

    s1.popLeft()
    s1.popLeft()
    s1.popLeft()

    print("Stack size: %s" % len(s1))
    print(s1.toList())



    print(-1%10)