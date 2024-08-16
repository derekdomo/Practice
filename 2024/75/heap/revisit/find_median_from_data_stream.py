'''
The median is the middle value in an ordered integer list. If the size of the 
list is even, there is no middle value, and the median is the mean of the two 
middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 
10-5 of the actual answer will be accepted.
'''

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        # all the larger values are in the minHeap
        # all the smaller values are in the maxHeap

    def addNum(self, num):
        import heapq
        if len(self.small) == 0 or len(self.big) == 0:
            heapq.heappush(self.small, -num)
        else:
            val_small = -self.maxHeap[0]
            val_big = self.minHeap[0]
            if num > val_small:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)



        if len(self.maxHeap) > len(self.minHeap)+1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        elif len(self.maxHeap) + 1 < len(self.minHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)




    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0]-self.maxHeap[0])/2.0
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]
