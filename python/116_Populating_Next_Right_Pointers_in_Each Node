# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        row = [root]
        while row:
            for i, p in enumerate(row):
                if i>0:
                    row[i-1].next = p
                if i==len(row)-1:
                    p.next = None
            row = [child for node in row for child in (node.left, node.right) if child]
