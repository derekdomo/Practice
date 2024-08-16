class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        heap = [(n.val, n) for n in lists]

        fake_head = ListNode(-1)
        cur = fake_head
        while len(heap) > 0:
            import heapq
            val, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next != None:
                heapq.heappush(heap, (node.next.val, node.next))
        
        return fake_head.next



