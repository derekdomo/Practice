class Solution:
    def generate_bracket_combinations(self, num_pairs):
        cur_res = ""
        res = []
        self.dfs_helper(num_pairs, num_pairs, cur_res, res)
        return res

    def dfs_helper(self, left, right, cur_res, res):
        if right == 0:
            res.append(cur_res)
            return
        if left > 0:
            self.dfs_helper(left-1, right, cur_res+"(", res)
        if left < right:
            self.dfs_helper(left, right-1, cur_res+")", res)

if __name__ == "__main__":
    sol = Solution()
    print sol.generate_bracket_combinations(3)

