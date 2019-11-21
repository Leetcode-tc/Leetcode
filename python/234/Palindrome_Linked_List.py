# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow = fast = head
        #[1,2]
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        last = None
        while cur:
            next = cur.next
            cur.next = last
            last = cur
            cur = next
        p1 = head
        p2 = last
        while p1 and p2 and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next
        return p2 == None
