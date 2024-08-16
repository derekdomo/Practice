class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2): 
        carry = 0
        fakeHead = ListNode(-1)
        cur = fakeHead
        while l1 != None or l2 != None:
            v = carry 
            if l1 != None:
                v += l1.val 
                l1 = l1.next
            if l2 != None:
                v += l2.val
                l2 = l2.next
            if v >= 10:
                cur.next = ListNode(v+carry-10)
                carry = 1
            else:
                cur.next = ListNode(v)
                carry = 0
            cur = cur.next

        if carry > 0:
            cur.next = ListNode(carry)

        return fakeHead.next()
