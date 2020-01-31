class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        ret = [[] for _ in range(numRows)]
        ret[0], ret[1] = [1], [1, 1]
        for i in range(2, numRows):
            ret[i] = [0 for _ in range(i+1)]
            ret[i][0], ret[i][-1] = 1, 1
            for j in range(1, i):
                ret[i][j] = ret[i-1][j-1] + ret[i-1][j]
        return ret
