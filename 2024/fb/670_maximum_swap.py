class Solution:
    def maximum_swap(self, num):
        nums = list(str(num))
        last_pos = {}
        for i, n in enumerate(nums):
            last_pos[int(n)] = i

        for i in range(len(nums)):
            for j in range(9, -1, -1):
                if j in last_pos and last_pos[j] > i and j > int(nums[i]):
                    k = last_pos[j]
                    nums[i], nums[k] = nums[k], nums[i]
                    return int("".join(nums))
        return num

sol = Solution()
print(sol.maximum_swap(3241))
