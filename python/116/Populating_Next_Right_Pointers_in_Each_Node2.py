"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
                
            self.connect(root.left)
            self.connect(root.right)
        return root
