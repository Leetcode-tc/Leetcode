class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not len(matrix) or not len(matrix[0]):
            return []
        m, n = len(matrix), len(matrix[0])
        up, down = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        ret  = []
        while len(ret) < m*n:
            for i in range(left, right+1):
                ret.append(matrix[up][i])
                if i == right:
                    up += 1
            for i in range(up, down+1):
                ret.append(matrix[i][right])
                if i == down:
                    right -= 1
            for i in range(right, left-1, -1):
                ret.append(matrix[down][i])
                if i == left:
                    down -= 1
            for i in range(down, up-1, -1):
                ret.append(matrix[i][left])
                if i == up:
                    left += 1
        return ret[:m*n]

