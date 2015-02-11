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

    def transferStack(self):
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

if __name__ == '__main__':
    ex = Exercises()
    s = Stack(22)
    print("Stack size: %s" % s.size())
    s.push(10)
    s.push(100)
    s.push(1000)
    print("Stack size: %s" % s.size())
    ex.emptyStackRecursively(s)
    print("Stack size: %s" % s.size())







