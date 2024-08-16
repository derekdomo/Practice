'''
Given the beginning of a linked list head, return true if there is a cycle in 
the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list that can be 
visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it 
exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        visited = {}
        cur = head
        while cur != None:
            if cur in visited:
                return True
            else:
                cur = cur.next

        return False

    def hasCycle(self, head):
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
