# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            if root.left is root.right:
                return root.val == sum
            else:
                return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        return False

# is: 判断两个变量的id是否相等
# ==: 判断两个变量的值是否相等
# x = y = [1,2,3,4]
# z = [1,2,3,4]
# x == z True
# x is z False
# x is y True  


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum -root.val) 