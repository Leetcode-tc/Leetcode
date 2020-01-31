"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        row = [root]
        while row:
            for i, p in enumerate(row):
                if i > 0:
                    row[i-1].next = p
                if i == len(row)-1:
                    p.next = None
            row = [child for node in row for child in (node.left, node.right) if child]
        return root
