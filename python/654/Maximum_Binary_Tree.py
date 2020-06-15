# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_val = max(nums)
        max_index = nums.index(max_val)
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return root

        # 递归
        # 先找到最大值以及最大值的位置max_index
        # 对于nums[:max_index]递归调用函数，返回值为root.left；对于nums[max_index+1:]递归调用函数，返回值为root.right
