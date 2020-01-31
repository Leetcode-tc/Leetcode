# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        d = collections.defaultdict(int)
        def preOrder(root):
            if root:
                d[root.val] += 1
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        cntList = sorted([(k,v) for k,v in d.items()], key=lambda x:x[1], reverse=True)
        res = [x[0] for x in cntList if x[1] == cntList[0][1]]
        return res        
