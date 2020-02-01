"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        maxD = 0
        for node in root.children:
            curD = self.maxDepth(node)
            if curD > maxD:
                maxD = curD 
        return maxD + 1
        
