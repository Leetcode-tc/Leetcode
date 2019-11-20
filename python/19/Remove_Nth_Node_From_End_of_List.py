tion for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n==0:
            return head
        newhead = ListNode(0)
        newhead.next = head
        p = pre = newhead
        for i in range(n):
            p = p.next
        while p.next:
            pre = pre.next
            p = p.next
        pre.next = pre.next.next
        return newhead.next
