class ExercisesException(Exception):
    """
    Exception class handling all exceptions.
    """
    pass

from Chapter6_Stacks_Queues.ArrayStack import Stack


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

if __name__ == '__main__':
    print(Exercises.reverseList((1,2,3,4)))