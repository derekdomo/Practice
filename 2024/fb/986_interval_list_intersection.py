class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        cur_first = 0
        cur_second = 0
        ret = []
        while cur_first < len(firstList) and cur_second < len(secondList):
            f = firstList[cur_first]
            s = secondList[cur_second]

            if f[0] > s[1]:
                cur_second += 1
            elif s[0] > f[1]:
                cur_first += 1
            else:
                ret +=  [[max(f[0], s[0]), min(f[1], s[1])]]
                if s[1] > f[1]:
                    cur_first += 1
                    secondList[cur_second] = [f[1]+1,s[1]]
                else:
                    cur_second += 1
                    firstList[cur_first] = [s[1]+1, f[1]]

        return ret
