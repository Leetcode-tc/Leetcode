class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        cnt = 0
        neighbor = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    cnt += 1
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        neighbor += 1
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        neighbor += 1
        res = cnt * 4 - neighbor *2 
        return res
