class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        memo = {}
        dummyHead = Node(-1)
        cur = dummyHead
        to_copy = head
        while to_copy != None:
            if to_copy in memo:
                cur.next = memo[to_copy]
            else:
                cur.next = Node(to_copy.val)
            cur = cur.next
            memo[to_copy] = cur
            # copy random
            to_copy_r = to_copy.random
            if to_copy_r is None:
                to_copy = to_copy.next
                continue
            if to_copy_r in memo:
                cur.random = memo[to_copy_r]
            else:
                cur.random = Node(to_copy_r.val)
            memo[to_copy_r] = cur.random
            to_copy = to_copy.next
        return dummyHead.next
            
