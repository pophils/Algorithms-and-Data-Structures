class ExercisesException(Exception):
    """
    Exception class handling all exceptions.
    """
    pass

from Chapter6_Stacks_Queues.ArrayStack import Stack
from Chapter6_Stacks_Queues.ArrayQueue import Queue


class Exercises():
    """
    Solutions to exercises of chapter 6 (Stacks and queues).
    """
    @staticmethod
    def __newStack(capacity=None):
        """
        Creates a new stack
        """
        return Stack(capacity)

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
            tempStack = Stack(seqLen)
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

        if not isinstance(r, Stack):
            raise ExercisesException("r is not a Stack type")
        if not isinstance(s, Stack):
            raise ExercisesException("s is not a Stack type")
        if not isinstance(t, Stack):
            raise ExercisesException("t is not a Stack type")

        if not t.isEmpty():
            tLen = t.size()
            r = t.transfer(r)
            while tLen > 0:
                s.push(r.pop())
                tLen -= 1


class QueuedStack():
    """
    C-6.24: Class implement a Stack ADT using a single Queue as an
    instance variable and only a constant memory within the
    method bodies
    """

    def __init__(self, queue=None, capacity=10):

        if queue is None:
            self.__queue = Queue(capacity)
        else:
            if not isinstance(queue, Queue):
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
        the underlying queue size needs to reduced.
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


if __name__ == '__main__':
    s1 = QueuedStack()

    print("Stack size: %s" % s1.size())
    print("-------------------------------------")
    print("-------------------------------------")

    s1.push(3)
    s1.push(20)
    s1.push(200)

    print("Stack size: %s" % s1.size())
    print("-------------------------------------")
    print("-------------------------------------")
    print("Top of stack: %s" % s1.top())

    s1.pop()
    s1.pop()

    print("-------------------------------------")
    print("-------------------------------------")
    print("Stack size: %s" % s1.size())
    print("Top of stack: %s" % s1.top())

    s1.push('westley Snipes')
    s1.push(20000000)
    s1.push(300)
    s1.push([1, 2, 3, 4, 5])

    print("-------------------------------------")
    print("-------------------------------------")
    print("Stack size: %s" % s1.size())
    print("Top of stack: %s" % s1.top())

    s1.pop()
    s1.pop()
    s1.pop()

    print("-------------------------------------")
    print("-------------------------------------")
    print("Stack size: %s" % s1.size())
    print("Top of stack: %s" % s1.top())
