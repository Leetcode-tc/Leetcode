# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        curSum = [0]
        def dfs(root):
            if root:
                dfs(root.right)
                root.val += curSum[0]
                curSum[0] = root.val
                dfs(root.left)
        dfs(root)
        return root
