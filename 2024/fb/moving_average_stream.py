'''
346. Moving Average from Data Stream
Easy
Topics
Companies
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
 

Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

Constraints:

1 <= size <= 1000
-105 <= val <= 105
At most 104 calls will be made to next.
'''
class MovingAverage:
    def __init__(self, size):
        from collections import deque
        self.arr = deque()
        self.sum = 0
        self.size = size

    def next(self, val):
        self.arr.append(val)
        self.sum += val
        if len(self.arr) > self.size:
            left = self.arr.popleft()
            self.sum -= left
            return self.sum/self.size
        return self.sum/len(self.arr)

mov = MovingAverage(3)

print(mov.next(1))
print(mov.next(10))
print(mov.next(3))
print(mov.next(5))


