"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stack = []
        p = head
        while p:
            if p.child:
                if p.next:
                    next = p.next
                    next.pre = None
                    stack.append(next)
                p.next = p.child
                p.child = None
                p.next.pre = p
            pre = p
            p = p.next
            if not p and len(stack)>0:
                node = stack.pop()
                pre.next = node
                node.pre = pre
                p = node
        return head
