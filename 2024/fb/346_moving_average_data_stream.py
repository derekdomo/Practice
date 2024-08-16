class MovingAverage:

    def __init__(self, size):
        self.arr = []
        self.size = []
        self.sum = 0

    def next(self, val):
        self.arr.append(val)
        self.sum += val
        if len(self.arr) > self.size:
            n = self.arr.pop(0)
            self.sum -= n
        return self.sum / len(self.size)
