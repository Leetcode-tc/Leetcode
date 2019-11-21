# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        def getLength(head):
            if not head:
                return 0
            p = head
            cnt = 0
            while p:
                cnt += 1
                p = p.next
            return cnt
        n1 = getLength(headA)
        n2 = getLength(headB)
        h1, h2 = headA, headB
        if n1 > n2:
            for _ in range(n1-n2):
                h1 = h1.next
        else:
            for _ in range(n2-n1):
                h2 = h2.next
        while h1 and h2:
            if h1 != h2:
                h1 = h1.next
                h2 = h2.next
            else:
                return h1
        return None
