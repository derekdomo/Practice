class Solution:
    def maxProduct(self, nums):
        max_product = -math.inf
        max_product_so_far = nums[0]
        min_product_so_far = nums[0] 

        for n in nums[1:]:
            tmp_max = max(n, n*max_product_so_far, n* min_product_so_far)
            min_product_so_far = min(n, n*max_product_so_far, n*max_product_so_far)
            max_product_so_far = tmp_max
            max_product = max(max_product_so_far, max_product)

        return max_product
