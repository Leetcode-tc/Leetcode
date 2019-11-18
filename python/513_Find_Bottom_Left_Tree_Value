# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :description:层序遍历树，row记录每一层节点的val，遍历完之后row[0]即是最后一层最左边的值
        """
        row = []
        q = [root]
        while q:
            row = [node.val for node in q]
            q = [child for node in q for child in (node.left, node.right) if child]
        return row[0]
