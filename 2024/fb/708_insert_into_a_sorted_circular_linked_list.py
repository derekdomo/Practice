class Solution:
    def insert(self, head, insertVal):
        if head == None:
            head = Node(insertVal)
            head.next = head
            return head
        if head.next == head:
            head.next = Node(insertVal, head)
            return head
        
        toInsert = False
        prev = head
        cur = head.next
        while True:
            if cur.val >= insertVal and prev.val <= insertVal:
                toInsert = True
            elif pre.val > cur.val:
                # we are at the end of the circle
                if insertVal >= pre.val or insertVal <= cur.val:
                    toInsert = True
            if toInsert:
                pre.next = Node(insertVal, cur)
                return head
            
            pre = cur
            cur = cur.next
            
            if pre == head:
                break

        # when outside of the loop, that means we can insert anywhere
        pre.next = Node(insertVal, cur)
        return head


