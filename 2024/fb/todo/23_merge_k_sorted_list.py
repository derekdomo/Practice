'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        import heapq
        for n in lists:
            if n != None:
                heapq.heappush(heap, (n.val, n))

        head = ListNode(-1)
        cur = head
        while len(heap) > 0:
            _, n = heapq.heappop(heap)
            cur.next = n
            cur = n
            if n.next != None:
                heapq.heappush(heap, (n.val, n))

        return head.next


