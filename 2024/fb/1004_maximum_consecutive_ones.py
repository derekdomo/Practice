class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # the tricky part is the boundary definition, what left means and what right means
        # can we assume left is always zero or one
        # consider the starting case
        # if we start with zero, left will be zero but right will flip it to one
        # so left is always one
        # how about right, right should always be zero
        left = 0
        right = 0
        remaining = k
        max_len = 0
        while right < len(nums):
            if nums[right] == 1:
                right += 1
            elif remaining > 0:
                remaining -= 1
                right += 1
            else:
                while left <= right:
                    if nums[left] == 1:
                        left += 1
                    else:
                        left += 1
                        remaining += 1
                        break
            max_len = max(max_len, right - left) 

sol = Solution()
ans = sol.longestOnes([])
print(ans)

