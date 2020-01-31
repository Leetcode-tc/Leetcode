"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        d = dict()
        def dfs(v):
            n = Node(v.val, [])
            d[v] = n
            for x in v.neighbors:
                if not x in d:
                    d[x] = dfs(x)
                n.neighbors.append(d[x])
            return n
        return dfs(node)
