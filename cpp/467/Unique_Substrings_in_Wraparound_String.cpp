class Solution {
public:
    int findSubstringInWraproundString(string p) {
        int dp[26] = {0};
        int lastPos = -1;
        for(int i=0;i<p.size();++i){
            if(i==0||(p[i-1]-'a'+1)%26+'a'!=p[i]){
                lastPos = i-1;
            }
            dp[p[i]-'a'] = max(dp[p[i]-'a'], i-lastPos);
        }
        return accumulate(dp, dp+26, 0);
    }
};
