# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        if not head:
            return 0
        p = head
        res = 0
        while p:
            res = res * 2 + p.val
            p = p.next
        return res
