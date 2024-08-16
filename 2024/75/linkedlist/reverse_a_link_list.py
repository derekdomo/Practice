class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, head):
        if head == None:
            return None
        fake_head = ListNode(-1)
        fake_head.next = head
        cur = head
        pre = fake_head
        while cur != None:
            t = cur.next
            cur.next = pre
            pre = cur
            cur = t

        head.next = None

        return pre 

