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




    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res =[]
        def dfs(stack, left, right):
            if left == right == n:
                res.append(''.join(stack))
                return
            if left < n:
                stack.append('(')
                dfs(stack, left+1, right)
                stack.pop()
            if right < n and right < left:
                stack.append(')')
                dfs(stack, left, right + 1)
                stack.pop()
        stack = []
        dfs(stack, 0, 0)
        return res


    # 动态规划
    def generateParenthesis3(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]

        dp = [None for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - 1 - j]
                for s1 in left:
                    for s2 in right:
                        cur.append('(' + s1 + ')' + s2)
            dp[i] = cur
        return dp[n]
