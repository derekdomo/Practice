class Solution:
    def findMedianSortedArrayB(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            return self.findKthElement(nums1, nums2, length/2+1)
        else:
            return (self.findKthElement(nums1, num2, length/2) + self.findKthElement(nums1, nums2, length/2+1))/2
    

    def findKthElement(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]

        if k == 1:
            return min(nums1[0], nums2[0])

        aVal = math.inf
        if k/2 <= len(nums1):
            aVal = nums1[k/2-1]
        bVal = math.inf
        if k/2 <= len(nums2):
            bVal = nums2[k/2-1]
        
        if aVal > bVal:
            if k/2 > len(nums2):
                nums2 = []
            else:
                nums2 = nums2[k/2:]
        else:
            if k/2 > len(nums1):
                nums1 = []
            else:
                nums1 = nums1[k/2:]

        return self.findKthElement(nums1, nums2, k-k/2)


    def findMedianSortedArray(self, nums1, nums2):
        import heapq
        # store values on the smaller side
        max_heap = []
        # store values on the larger side
        min_heap = []

        cur1 = 0
        cur2 = 0
        while cur1 < len(nums1) or cur2 < len(nums2):
            if cur2 == len(nums2):
                if len(max_heap) == 0:
                    heapq.heappush(min_heap, nums1[cur1])
                    cur1 += 1
                else:
                    if nums1[cur1] < min_heap[0]:
                        heapq.heappush(max_heap, -nums1[cur1])
                    else:
                        heapq.heappush(min_heap, nums1[cur1])
                    cur1 += 1
            elif cur1 == len(nums1):
                if len(max_heap) == 0:
                    heapq.heappush(min_heap, nums2[cur2])
                    cur2 += 1
                else:
                    if nums2[cur2] < min_heap[0]:
                        heapq.heappush(max_heap, -nums2[cur2])
                    else:
                        heapq.heappush(min_heap, nums2[cur2])
                    cur2 += 1
            else:
                n = None
                if nums1[cur1] > nums2[cur2]:
                    n = nums2[cur2]
                    cur2 += 1
                else:
                    n = nums1[cur1]
                    cur1 += 1

                if len(max_heap) == 0:
                    heapq.heappush(min_heap, n)

            if len(min_heap) > len(max_heap) + 1:
                n = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -n)
            elif len(min_heap) + 1 < len(max_heap):
                n = heapq.heappop(max_heap)
                heapq.heappush(min_heap, -n)

        if len(max_heap) == len(min_heap):
            return (min_heap[0] - max_heap[0]) /2
        elif len(max_heap) == len(min_heap) + 1:
            return -max_heap[0]
        else:
            return min_heap[0]

sol = Solution()
print(sol.findMedianSortedArray([1,2], [3,4]))

