class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # dp[i][j] 表示[i,j]先拿者能赢的最大分数，dp[i][j]=max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
        # 先求子问题，l表示长度 1~n
        for i in range(n):
            dp[i][i] = piles[i]
        for l in range(2, n+1):
            i = 0
            j = i+l-1
            while j<n:
                dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
                i += 1
                j = i+l-1
        return dp[0][n-1] > 0
