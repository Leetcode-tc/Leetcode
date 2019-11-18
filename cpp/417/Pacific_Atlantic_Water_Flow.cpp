class Solution {
public:
    vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
        vector<pair<int, int>> ret;
        if(matrix.size()==0) return ret;
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        for(int i=0;i<m;++i){
            solve(matrix, pacific, i, 0);
            solve(matrix, atlantic, i, n-1);
        }
        
        for(int j=0;j<n;++j){
            solve(matrix, pacific, 0, j);
            solve(matrix, atlantic, m-1, j);
        }
        
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(pacific[i][j]&&atlantic[i][j])
                    ret.push_back(make_pair(i, j));
            }
        }
        return ret;
    }
    
    void solve(vector<vector<int>>& matrix, vector<vector<bool>> &ocean, int i, int j){
        ocean[i][j] = true;
        int dx[4] = {-1,0,1,0}, dy[4] = {0,-1,0,1};
        for(int k=0;k<4;++k){
            int nx = i+dx[k], ny = j+dy[k];
            if(nx>=0&&nx<matrix.size()&&ny>=0&&ny<matrix[nx].size()&&matrix[i][j]<=matrix[nx][ny]&&!ocean[nx][ny]){
                solve(matrix, ocean, nx, ny);
            }
        }
    }
};
