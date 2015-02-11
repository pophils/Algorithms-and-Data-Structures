class ProblemsException(Exception):
    """
    This is the exception class handling all exceptions that occurs
    in all the exercises.
    """
    pass


class Problems():
    pass

    @staticmethod
    def TestComprehension(seq=[]):
        """
            :type seq: a list object
            Using  comprehension over append in a for loop is faster as
            the list elements is prepared and used to construct the list at once
            unlike append that leads to multiple resizing of the underlying array.
        """
        import datetime as DT

        testArray = [12, 11, 11, 101, 198, 534, 12, 11, 11, 101, 198, 534, 432, 190, 312, 567, 352, 10000, 2109,
                     12, 11, 11, 101, 198, 534, 12, 11, 11, 101, 198, 534, 432, 190, 312, 567, 352, 10000, 2109,
                     12, 11, 11, 101, 198, 534, 12, 11, 11, 101, 198, 534, 432, 190, 312, 567, 352, 10000, 2109,
                     12, 11, 11, 101, 198, 534, 12, 11, 11, 101, 198, 534, 432, 190, 312, 567, 352, 10000, 2109,
                     12, 11, 11, 101, 198, 534, 12, 11, 11, 101, 198, 534, 432, 190, 312, 567, 352, 10000, 2109,
                     12, 11, 11, 101, 198, 534, 12, 11, 11, 101, 198, 534, 432, 190, 312, 567, 352, 10000, 2109]

        startTime = DT.datetime.now()
        #for i in testArray:
        #    seq.append(i)

        seq = [x for x in testArray]
        endTime = DT.datetime.now()

        print("Number of input: %s" % len(seq))
        print("Execution time in seconds: %s" % (endTime - startTime).total_seconds())
        print(seq)

    @staticmethod
    def testCount():
        """
        Count runs in O(n) time complexity
        :return:
        """
        import datetime as DT

        testArray = [12, 11, 11, 101, 198, 534, 12, 11, 11, 101, 198, 534, 432, 190, 312, 567, 352, 10000, 2109,
                     12, 11, 11, 101, 198, 534, 12, 11, 11, 101, 198, 534, 432, 190, 312, 567, 352, 10000, 2109,
                     12, 11, 11, 101, 198, 534, 12, 11, 11, 101, 198, 534, 432, 190, 312, 567, 352, 10000, 2109,
                     12, 11, 11, 101, 198, 534, 12, 11, 11, 101, 198, 534, 432, 190, 312, 567, 352, 10000, 2109,
                     'xxx']

        startTime = DT.datetime.now()
        count = testArray.count('xxx')
        endTime = DT.datetime.now()

        print(count)
        print("Number of input: %s" % len(testArray))
        print("Execution time in seconds: %s" % (endTime - startTime).total_seconds())


if __name__ == '__main__':
    Problems.testCount()




