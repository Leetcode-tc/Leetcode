class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        
        for(auto s:strs){
            int numOfZeros = 0, numOfOnes = 0;
            for(auto c:s){
                if(c=='0'){
                    numOfZeros++;
                }
                else{
                    numOfOnes++;
                }
            }
            
            for(int i=m;i>=numOfZeros;--i){
                for(int j=n;j>=numOfOnes;--j){
                    dp[i][j] = max(dp[i][j], dp[i-numOfZeros][j-numOfOnes]+1);
                }
            }
        }
        
        return dp[m][n];
    }
};
