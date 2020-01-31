# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        position = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:position], postorder[:position])
        root.right = self.buildTree(inorder[position+1:], postorder[position:-1])
        return root
