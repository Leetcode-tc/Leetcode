# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append('Null')
            else:
                res.append(str(root.val))
                leftSerialize = dfs(root.left)
                rightSerialize = dfs(root.right)
        dfs(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        strs = iter(data.split(','))
        def dfs():
            val = next(strs)
            if val == 'Null':
                return None
            root = TreeNode(val)
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()     

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
