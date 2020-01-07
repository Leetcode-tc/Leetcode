# 思路：
# 两个节点p,q分为两种情况：
#       p和q在相同子树中
#       p和q在不同子树中
# 从根节点遍历，递归向左右子树查询节点信息
# 递归终止条件：如果当前节点为空或等于p或q，则返回当前节点
#
# 递归遍历左右子树，如果左右子树查到节点都不为空，则表明p和q分别在左右子树中，因此，当前节点即为最近公共祖先；
# 如果左右子树其中一个不为空，则返回非空节点。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if right == None:
            return left
        if left == None:
            return right
        
