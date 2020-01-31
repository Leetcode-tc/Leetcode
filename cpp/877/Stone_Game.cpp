class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        vector<vector<int>> dp(piles.size(), vector<int>(piles.size(), 0));
        for(int i=0;i<piles.size();++i){
            dp[i][i] = piles[i];
        }
        for(int i=2;i<=piles.size();++i){
            for(int j=0;j+i-1<piles.size();++j){
                dp[j][j+i-1] = max(piles[j]-dp[j+1][j+i-1], piles[j+i-1]-dp[j][j+i-2]);
            }
        }
        return dp[0][piles.size()-1]>0;
    }
};