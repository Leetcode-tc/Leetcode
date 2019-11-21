class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        //f[i][v]表示用前i种硬币组合成金额为v需要的最少硬币数
        //f[i][v] = min(f[i-1][v], f[i][v-coins[i]]+1, f[i-1][v-coins[i]]+1)
        //f[v] = min(f[v], f[v-coins[i]]+1)
        vector<int> dp(amount+1, amount+1);
        dp[0] = 0;
        for(int i=0;i<coins.size();++i){
            for(int j=coins[i];j<=amount;++j){
                dp[j] = min(dp[j], dp[j-coins[i]]+1);
            }
        }
        return dp[amount]==amount+1?-1:dp[amount];
    }
};