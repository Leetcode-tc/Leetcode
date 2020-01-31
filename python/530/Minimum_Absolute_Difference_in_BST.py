# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def inOrder(root):
            if root:
                inOrder(root.left)
                res.append(root.val)
                inOrder(root.right)
        inOrder(root)
        minDiff = 2**31-1
        for i in range(1,len(res)):
            if minDiff > (abs(res[i]-res[i-1])):
                minDiff = abs(res[i]-res[i-1])
        return minDiff