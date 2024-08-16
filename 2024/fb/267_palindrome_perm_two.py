from typing import List
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        from collections import Counter
        counter = Counter(s)
        odd_k = None
        for k, v in counter.items():
            if v % 2 == 1:
                if odd_k != None:
                    return []
                odd_k = k
        ret = set()
        def dfs(r_c, cur, ret):
            if len(r_c) == 0:
                ret.add(cur)
            for k, v in r_c.items():
                r_c_c = r_c.copy()
                if v == 2:
                    del r_c_c[k]
                else:
                    r_c_c[k] -= 2
                dfs(r_c_c, k+cur+k, ret)
        if odd_k != None:
            dfs(counter, odd_k, ret)
        else:
            dfs(counter, "", ret)
        return list(ret)

sol = Solution()
print(sol.generatePalindromes("aabb"))
print(sol.generatePalindromes("abc"))
        
