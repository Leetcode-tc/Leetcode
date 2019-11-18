class Solution {
public:
    //dp[i][j][k]表示长度为i，'A'的个数为0，结尾'L'的个数为k的总数量
    //dp[i][0][0] = sum(dp[i-1][0]),     以'P'结尾
    //dp[i][0][1] = dp[i-1][0][0]
    //dp[i][0][2] = dp[i-1][0][1]
    //dp[i][1][0] = sum(dp[i-1][1])+sum(dp[i-1][0])
    //dp[i][1][1] = dp[i-1][1][0]
    //dp[i][1][2] = dp[i-1][1][1]
    int checkRecord(int n) {
        long long dp[2][2][3] = {{{1,1,0}, {1,0,0}}};
        int m = pow(10, 9)+7;
        for(int i=1;i<n;++i){
            int cur = i%2, prev = (i-1)%2;
            dp[cur][0][0] = accumulate(dp[prev][0], dp[prev][0]+3, 0L)%m;
            dp[cur][0][1] = dp[prev][0][0];
            dp[cur][0][2] = dp[prev][0][1];
            dp[cur][1][0] = (accumulate(dp[prev][1], dp[prev][1]+3, 0L)%m + accumulate(dp[prev][0], dp[prev][0]+3, 0L)%m)%m;
            dp[cur][1][1] = dp[prev][1][0];
            dp[cur][1][2] = dp[prev][1][1];
        }
        int index = (n-1)%2;
        return (accumulate(dp[index][0], dp[index][0]+3, 0L)%m+accumulate(dp[index][1], dp[index][1]+3, 0L)%m)%m;
    }
};
