class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n == 0:
            return [""]
        def dfs(tmp, left, right):
            if left==0 and right==0:
                res.append(tmp)
            if left > 0:
                dfs(tmp+'(', left-1, right)
            if right > 0 and left < right:
                dfs(tmp+')', left, right-1)
        dfs('', n, n)
        return res
