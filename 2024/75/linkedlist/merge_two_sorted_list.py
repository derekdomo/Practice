class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        cur1 = list1
        cur2 = list2
        head = ListNode(0)
        cur = head
        while cur1 != None and cur2 != None:
            if cur1 == None:
                cur.next = cur2
            elif cur2 == None:
                cur.next = cur1
            else:
                if cur1.val > cur2.val:
                    cur.next = cur2
                    cur2 = cur2.next
                else:
                    cur.next = cur1
                    cur1 = cur1.next

        return head.next
    

