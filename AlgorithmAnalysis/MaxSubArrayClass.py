
import datetime as DT


class MaxSubArray():
    """Programs compute indices i,j of an array such that
       sub array a[i:j] maximizes the sum of its values.
    """
    def __init__(self, array):
        if len(array) < 1:
            raise ValueError("The array must have at least one element")
        self.numArray = array
        self.arrayLen = len(array)
        self.MaxSum = 0
         
    def ComputeMaxSubArrayWithoutPrefixSums(self):
        """This algorithm is quadratic O(n**2) [5n2 + 3n + 1].
           Its a way faster than ComputeMaxSubArrayViaPrefixSums() which also is quadratic.
        """
        startTime = DT.datetime.now()
        for index in range(self.arrayLen):  # O(n)
            tempSum = 0
            tempIndex = index
            # the while loop will be executed based on the current value of the index and the value of arrayLen, n
            # summation of n +....+ 1 A.P series n(n+1) / 2 === O(n**2) quadratic complexity
            while tempIndex < self.arrayLen:  # O(n**2) quadratic complexity
                tempSum += self.numArray[tempIndex]  # O(n**2) quadratic complexity
                if tempSum > self.MaxSum:  # O(n**2) quadratic complexity
                    self.MaxSum = tempSum  # O(n**2) quadratic complexity
                tempIndex += 1  # O(n**2) quadratic complexity

        endTime = DT.datetime.now()
        print("Execution with aggregated sum in seconds: ", (endTime - startTime).total_seconds())
        print("Number fo elements, n: ", self.arrayLen)
        return self.MaxSum  # O(1) constant

    def ComputeMaxSubArrayViaPrefixSums(self):
        """This algorithm is quadratic O(n**2) [6n2 + 5n + 2].
           Its a bit slower than ComputeMaxSubArrayWithoutPrefixSums() which also is quadratic
           The computation of the prefix sums at the start of the method makes the
           running time grows with the size, n of the problem(Array) as compared with ComputeMaxSubArrayWithoutPrefixSums
        """
        startTime = DT.datetime.now()
        prefixSums = []
        for index in range(self.arrayLen):  # O(n)
            if index == 0:  # O(n)
                prefixSums.append(self.numArray[index])
            else:
                prefixSums.append(prefixSums[index - 1] + self.numArray[index])
             
        for index in range(self.arrayLen):  # O(n)
            tempIndex = index  # O(n)
            # the while loop will be executed based on the current value of the index and the value of arrayLen, n
            # summation of n +....+ 1 A.P series n(n+1) / 2 === O(n**2) quadratic complexity
            while tempIndex < self.arrayLen:  # O(n**2) quadratic complexity
                # O(n**2) quadratic complexity
                if index == 0:
                    tempSum = prefixSums[tempIndex]
                else:
                    tempSum = prefixSums[tempIndex] - prefixSums[index - 1]
                     
                if tempSum > self.MaxSum:  # O(n**2) quadratic complexity
                    self.MaxSum = tempSum  # O(n**2) quadratic complexity
                tempIndex += 1  # O(n**2) quadratic complexity
        
        endTime = DT.datetime.now()
        print("Execution with prefix sum in seconds: ", (endTime - startTime).total_seconds())
        print("Number fo elements, n: ", self.arrayLen)
        return self.MaxSum  # O(1) constant

    def ComputeMaxSubArrayLinearly(self):
        """This algorithm is linear O(n).
           Its a bit faster than ComputeMaxSubArrayLinearly2() as it generates 
           the prefix sum without making any comparison with 0 as done by the latter.   
           Its the fastest of the four algorithm         
        """
        startTime = DT.datetime.now()
        prefixSums = []
        for index in range(self.arrayLen):  # O(n)
            if index == 0:  # O(n)
                prefixSums.append(self.numArray[index])
            else:
                prefixSums.append(prefixSums[index - 1] + self.numArray[index])  
                       
        self.MaxSum = max(prefixSums) - min(prefixSums)
         
        endTime = DT.datetime.now()

        print("Execution via ComputeMaxSubArrayLinearly() in seconds: ", (endTime - startTime).total_seconds())
        print("Number fo elements, n: ", self.arrayLen)
        return self.MaxSum  # O(1) constant

    def ComputeMaxSubArrayLinearly2(self):
        """This algorithm is linear O(n).
           Its a lil' bit slower than ComputeMaxSubArrayLinearly().     
        """
        startTime = DT.datetime.now()
        prefixMax = []
        for index in range(self.arrayLen):  # O(n)

            # the next max subarray will definitely be the currentmax term
            # plus the next term in the series
            if index == 0:
                prefixMax.append(max(0, self.numArray[index]))
            else:
                prefixMax.append(max(0, (prefixMax[index - 1] + self.numArray[index])))
        self.MaxSum = max(prefixMax)  # O(1) constant

        endTime = DT.datetime.now()
        print("Execution with ComputeMaxSubArrayLinearly2() in seconds: ", (endTime - startTime).total_seconds())
        print("Number fo elements, n: ", self.arrayLen)

        return max(prefixMax)  # O(1) constant


if __name__ == "__main__":
    print("Maximum Sub Array sum of [0,1,2,3,4,5,6,7,8,9] is %s " % MaxSubArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).
          ComputeMaxSubArrayLinearly())