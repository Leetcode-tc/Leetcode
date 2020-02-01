# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def dfs(root):
            if root:
                rl = dfs(root.left)
                rr = dfs(root.right)
                res[0] += abs(rl-rr)
                return root.val + rl + rr
            return 0
        dfs(root)
        return res[0]
        
