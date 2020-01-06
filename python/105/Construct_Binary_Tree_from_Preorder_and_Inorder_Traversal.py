# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not preorder:
            return None
        root = TreeNode(preorder[0])
        position = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:position+1], inorder[:position])
        root.right = self.buildTree(preorder[position+1:], inorder[position+1:])
        return root
