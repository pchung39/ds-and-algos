from heapq import * 


class KthLargestNumberInStream:
    min_heap = []

    def __init__(self, stream, k):

        self.k = k

        for num in stream:
            self.add(num)

    def add(self, num):

        # this function will add a number to the heap 
        # use a min heap because we need to find the kth largest element 
        # this essentially means that we want the kth largest from the 
        # beginning of the list

        # push number to heap
        heappush(self.min_heap, num)

        # make sure to keep the size of the heap within k 
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

        # return kth largest number 
        return self.min_heap[0]

def main():

    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()