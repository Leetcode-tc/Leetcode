# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n = self.getLength(head)
        if not head or not head.next or k%n == 0:
            return head
        k %= n
        pre = cur = head
        for _ in range(k):
            cur = cur.next
        while cur.next:
            pre = pre.next
            cur = cur.next
        newhead = pre.next
        pre.next = None
        cur.next = head
        return newhead
     
    def getLength(self, head):
        cnt = 0
        p = head
        while p:
            cnt += 1
            p = p.next
        return cnt
