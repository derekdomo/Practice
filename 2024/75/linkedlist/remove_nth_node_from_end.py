'''
Given the head of a linked list, remove the nth node from the end of the list 
and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def solve(self, head, n):
        fake_head = ListNode(-1)
        cur = head

        for i in range(n):
            cur = cur.next

        # now cur is the nth node from the beginning 

        n_pre = fake_head
        n_cur = node
        while cur != None:
            n_pre = n_cur
            n_cur = n_cur.next
            cur = cur.next

        # now n_cur should the be nth node from the end

        n_pre.next = cur.next
        cur.next = None
        
        return head
