class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        row, col = len(grid), len(grid[0])
        tmp = [0] * (row*col)
        for i in range(row):
            for j in range(col):
                k %= row*col
                tmp[k] = grid[i][j]
                k += 1
        for i in range(row):
            for j in range(col):
                grid[i][j] = tmp.pop(0)
        return grid
