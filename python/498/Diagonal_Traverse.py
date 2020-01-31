class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        row = len(matrix)
        col = len(matrix[0])
        digits = [[] for _ in range(row+col-1)]
        for i in range(row):
            for j in range(col):
                digits[i+j].append(matrix[i][j])
        ret = []
        for k in range(row+col-1):
            if k%2 == 0:
                ret.extend(digits[k][::-1])
            else:
                ret.extend(digits[k])
        return ret


    def findDiagonalOrder2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        dx = [-1, 1]
        dy = [1, -1]
        d = 0   # shang
        ret = []
        x,y = 0, 0
        row = len(matrix)-1
        col = len(matrix[0])-1
        while 0<=x<=row and 0<=y<=col:
            ret.append(matrix[x][y])
            need_move = True
            if (d == 0 and x == 0) or (d == 1 and x == row):
                d = 1 ^ d   # d = 1-d
                y += 1
                if y <= col:
                    need_move = False
            elif (d == 0 and y == col) or (d == 1 and y == 0):
                d = 1 ^ d
                x += 1
                if x <= row:
                    need_move = False
            if need_move:
                x += dx[d]
                y += dy[d]
        return ret
