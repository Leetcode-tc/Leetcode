# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p1 = left = ListNode(0)
        p2 = right = ListNode(0)
        cur = head
        while cur:
            if cur.val < x:
                p1.next = cur
                cur = cur.next
                p1 = p1.next
            else:
                p2.next = cur
                cur = cur.next
                p2 = p2.next
        p2.next = None
        p1.next = right.next 
        return left.next
