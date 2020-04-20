class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        fast, slow = head.next, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.next.val)
        
