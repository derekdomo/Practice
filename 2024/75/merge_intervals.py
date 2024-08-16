class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, lambda i: i[0])
        ret = []
        for i in range(1, len(intervals)):
            if interval[i-1][1] < interval[i][0]:
                ret.append(interval[i-1])
            else:
                interval[i][0] = min(interval[i][0], interval[i-1][0])
                interval[i][1] = max(interval[i][1], interval[i-1][1])

        ret.append(interval[-1])
        return ret
        
