'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None
        reversed_head = reverse(slow)

        return merge_two_lists(head, reverse_head)

    
    def merge_two_list(self, cur1, cur2):
        fake_head = ListNode(-1)
        cur = fake_head
        while cur1 != None and cur2 != None:
            cur.next = cur1
            cur1 = cur1.next
            cur = cur.next
            cur.next = cur2
            cur2 = cur2.next
            cur = cur.next

        return fake_head.next

    
    def reverse(self, node):
        fake_head = ListNode(-1)
        fake_head.next = node
        pre = fake_head
        cur = node

        while cur is not None:
            t = cur.next
            cur.next = pre
            prev = cur
            cur = t

        node.next = None
        return prev
    

