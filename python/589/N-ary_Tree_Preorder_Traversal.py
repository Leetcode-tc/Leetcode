"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        def dfs(root):
            if root:
                res.append(root.val)
                for node in root.children:
                    dfs(node)
        dfs(root)
        return res
