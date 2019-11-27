class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        ret = 0
        for i in range(row):
            for j in range(col):
                if int(grid[i][j]):
                    q = []
                    ret += 1
                    # BFS
                    # 将根结点压入队列
                    q.append((i, j))
                    # 开始循环
                    while len(q) > 0:
                        # 取出一个节点
                        x, y = q.pop()
                        grid[x][y] = '0'
                        # 放入周围节点
                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            if 0<=nx<row and 0<=ny<col and grid[nx][ny]=='1':
                                q.append((nx, ny))
        return ret
