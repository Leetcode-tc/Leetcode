class Solution(object):
    def dfs(self, grid, x, y):
        grid[x][y] = '0'
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        row, col = len(grid), len(grid[0])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == '1':
                self.dfs(grid, nx, ny)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        ret = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    ret += 1
                    self.dfs(grid, i, j)
        return ret
