# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        myQueue = [root]
        while myQueue:
            res = []
            for _ in range(len(myQueue)):
                node = myQueue.pop(0)
                res.append(node.val)
                if node.left:
                    myQueue.append(node.left)
                if node.right:
                    myQueue.append(node.right)
            result.append(res)
        return result
