class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        res = [[0 for _ in range(m)] for _ in range(n)]
        for k in indices:
            row, col = k[0], k[1]
            for j in range(m):
                res[row][j] += 1
            for i in range(n):
                res[i][col] += 1
        cnt = 0        
        for i in range(n):
            for j in range(m):
                if res[i][j] % 2 == 1:
                    cnt +=1
        return cnt
