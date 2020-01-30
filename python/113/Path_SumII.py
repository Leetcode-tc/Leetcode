# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        stack = []
        def dfs(root, sum):
            if root:
                stack.append(root.val)
                if root.left is root.right and root.val == sum:
                    # 拷贝一份新的stack
                    res.append(list(stack))
                dfs(root.left, sum - root.val) 
                dfs(root.right, sum - root.val)
                stack.pop()
        dfs(root, sum)
        return res
