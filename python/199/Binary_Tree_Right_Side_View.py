# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #层序遍历，记录每层最后一个数
        if not root: return []
        ret = []
        row = [root]
        while row:
            ret.append(row[-1].val)
            row = [child for node in row for child in (node.left, node.right) if child]
        return ret
