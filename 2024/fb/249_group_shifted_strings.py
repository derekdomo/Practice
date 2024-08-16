from typing import List
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        from collections import defaultdict
        def cal_hash(s):
            c = s[0]
            diff = ord(c) - ord('a')
            ret = []
            for c in s:
                n_c = ord(c) - diff
                if n_c < ord('a'):
                    n_c += 26
                ret.append(chr(n_c))
            return "".join(ret)

        hash_dict = defaultdict(list)
        for s in strings:
            if len(s) == 1:
                hash_dict[(1, 'a')].append(s)
            else:
                hash = cal_hash(s)
                hash_dict[(len(s), hash)].append(s)

        return hash_dict.values()

sol = Solution()
q = ["abc","bcd","acef","xyz","az","ba","a","z"]
print(sol.groupStrings(q))

