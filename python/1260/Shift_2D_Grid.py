class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        row, col = len(grid), len(grid[0])
        res = [[None for _ in range(col)] for _ in range(row)]
        for c in range(k):
            for i in range(row):
                for j in range(col):
                    if j == col-1:
                        if i == row-1:
                            res[0][0] = grid[row-1][col-1]
                        else :
                            res[i+1][0] = grid[i][col-1]
                    else:
                        res[i][j+1] = grid[i][j]             
            grid = copy.deepcopy(res)
        return grid



# wrong solution
