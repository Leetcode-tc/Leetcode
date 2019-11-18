class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int ret = 0;
        for(int i=0;i<grid.size();i++){
            for(int j=0;j<grid[i].size();j++){
                if(grid[i][j]=='1'){
                    solve(grid, i, j);
                    ret++;
                }
            }
        }
        return ret;
    }
    
    void solve(vector<vector<char>> &grid, int i, int j){
        grid[i][j] = '0';
        int dx[4] = {-1,0,1,0}, dy[4] = {0,-1,0,1};
        for(int k=0;k<4;++k){
            int nx = i+dx[k], ny = j+dy[k];
            if(nx>=0&&nx<grid.size()&&ny>=0&&ny<grid[nx].size()&&grid[nx][ny]=='1'){
                solve(grid, nx, ny);
            }
        }
    }
};
