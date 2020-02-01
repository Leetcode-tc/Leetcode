# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        res = []
        cnt = 0
        if not head:
            return []
        while head:
            while stack and stack[-1][0] < head.val:
                res[stack[-1][1]] = head.val
                stack.pop()
            stack.append([head.val, cnt])
            head = head.next
            cnt += 1
            res.append(0)
        return res
        