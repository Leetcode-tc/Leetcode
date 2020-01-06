# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        myQueue = []
        myQueue.append(root)
        cnt = 0
        while myQueue:
            res = []
            for _ in range(len(myQueue)):
                node = myQueue.pop(0)
                if node.left:
                    myQueue.append(node.left)
                if node.right:
                    myQueue.append(node.right)                   
                res.append(node.val)
            cnt += 1
            if cnt & 1 == 1:
                result.append(res)
            else:
                result.append(res[::-1])
        return result

