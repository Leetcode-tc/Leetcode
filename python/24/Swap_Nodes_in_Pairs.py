# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newhead = ListNode(0)
        newhead.next = head
        pre = newhead
        p = head
        while p and p.next:
            next = p.next
            pre.next = next
            p.next = next.next
            next.next = p
            pre = p
            p = p.next
        return newhead.next

