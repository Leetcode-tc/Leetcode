class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        newhead = ListNode(0)
        newhead.next = head
        pre, p = newhead, head
        while p:
            if p.val != val:
                pre = pre.next
                p = p.next
            else:
                pre.next = p.next
                p = pre.next
        return newhead.next
