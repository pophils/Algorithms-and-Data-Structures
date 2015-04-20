
from AbstractBases.PriorityQueue import PriorityQueue as abstractPQ
from AppException.PriorityQueueException import PriorityQueueException

class ArraySortedPriorityQueue(abstractPQ):
    """
    Class provides an array based implementation of a sorted priority Queue.
    Each item is removed in constant O(1) time while inserting a new element is done in O(n) time
    """

    def __init__(self, order=0, capacity=None, dType=int):
        """
        Init the queue
        :param order: The order at which items are removed from the queue. 0=Min, 1=Max
        """
        if not isinstance(order, int):
            raise TypeError("order must be a number.")
        if capacity is not None and not isinstance(order, int):
            raise TypeError("capacity must be a number.")

        self.__capacityGiven = False
        self.__data = []
        self.__dType = dType
        self.__currentHead = 0

        if order > 0:
            self.__isMin = False
        else:
            self.__isMin = True

        if capacity is not None:
            self.__capacityGiven = True
            self.__capacity = capacity

    def __validateDType(self, e):
        """
        Validate each item type against the supplied type at __init__
        :param e: item
        """
        if type(e) != self.__dType:
            raise TypeError("element of the queue must be of type %s" % self.__dType)

    def insert(self, e):
        """
        Insert new item to the priority queue
        Runs in O(n) time, where n is the number of element in the queue at the point of insertion.
        Search for the proper location runs in O(logn) time (binary search)
        :param e: item to be added
        :exception raise a PriorityQueueException if the capacity is given at instantiation and the
                   current size of the queue is equals the given capacity.
        """
        self.__validateDType(e)

        if self.__capacityGiven:
            if len(self.__data) == self.__capacity:
                raise PriorityQueueException("The queue is already full.")
        if self.isEmpty():
            self.__data.append(e)
        else:
            expectedIndex = self.__findIndex(0, len(self.__data) - 1, e)


            if self.__isMin: # sort from highest to lowest to ensure O(1) removal time
                immediateLeft = expectedIndex - 1

                if expectedIndex < len(self.__data) and self.__data[expectedIndex] == e:
                    tempData = self.__data[:expectedIndex]
                    tempData.append(e)
                    tempData.extend(self.__data[expectedIndex:])

                elif immediateLeft >= 0 and e >= self.__data[immediateLeft]:
                        tempData = self.__data[:immediateLeft]
                        tempData.append(e)
                        tempData.extend(self.__data[immediateLeft:])
                elif self.__data[expectedIndex] > e:
                    tempData = self.__data[:expectedIndex+1]
                    tempData.append(e)
                    tempData.extend(self.__data[expectedIndex+1:])
                else:
                    tempData = self.__data[:expectedIndex]
                    tempData.append(e)
                    tempData.extend(self.__data[expectedIndex:])

            else: # sort from lowest to highest to ensure O(1) removal time
                immediateRight = expectedIndex + 1

                if expectedIndex < len(self.__data) and self.__data[expectedIndex] == e:
                    tempData = self.__data[:expectedIndex]
                    tempData.append(e)
                    tempData.extend(self.__data[expectedIndex:])

                elif immediateRight <= len(self.__data) - 1 and e >= self.__data[immediateRight]:
                        tempData = self.__data[:immediateRight+1]
                        tempData.append(e)
                        tempData.extend(self.__data[immediateRight+1:])

                elif self.__data[expectedIndex] < e:
                    tempData = self.__data[:expectedIndex+1]
                    tempData.append(e)
                    tempData.extend(self.__data[expectedIndex+1:])
                else:
                    tempData = self.__data[:expectedIndex]
                    tempData.append(e)
                    tempData.extend(self.__data[expectedIndex:])

            self.__data = tempData

    def removeTop(self):
        """
        Removes the tail of the queue. Runs in O(1) time.
        :return: Object
        :exception raise PriorityQueueException if queue is empty
        """

        if self.isEmpty():
            raise PriorityQueueException("The queue is empty.")

        return self.__data.pop()

    def isEmpty(self):
        return len(self.__data) == 0

    def clear(self):
        self.__data = []     

    def peekTop(self):
        """
        Runs in constant O(1) time
        :return: object
        """
        if self.isEmpty():
            raise PriorityQueueException("The queue is empty.")

        return self.__data[len(self.__data) - 1]

    def size(self):
        return len(self.__data)

    def __len__(self):
        return len(self.__data)

    def __findIndex(self, firstIndex, lastIndex, targetItem):

        if firstIndex == lastIndex:
            return lastIndex
        if firstIndex > lastIndex and lastIndex <= 0:
            return 0
        elif firstIndex > lastIndex and lastIndex > 0:
            return lastIndex
        else:
            midIndex = (lastIndex + firstIndex) // 2

            if self.__data[midIndex] == targetItem:
                    return midIndex
            if self.__isMin:
                if self.__data[midIndex] < targetItem:
                    return self.__findIndex(firstIndex, midIndex - 1, targetItem)
                else:
                    return self.__findIndex(midIndex + 1, lastIndex, targetItem)
            else:
                if self.__data[midIndex] < targetItem:
                    return self.__findIndex(midIndex + 1, lastIndex, targetItem)
                else:
                    return self.__findIndex(firstIndex, midIndex - 1, targetItem)



if __name__ == '__main__':
    queue = ArraySortedPriorityQueue(order=0, dType=int)
    a = [120347372882, -1, -1, -0, -0, -109, -34, 9708, -1102, 23, 90, 90, 21, 10,-11, 12, 10000, 0, -12, 212, 100000012, -12903, 1109, -109,10, 23, 45, -1, 2, 0, 1, 1, 78]

    for i in range(len(a)):
        queue.insert(a[i])

    b = [queue.removeTop() for i in range(len(queue))]




    print(a)
    print(b)






