class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        if(wordDict.size()==0) return false;
        sort(wordDict.begin(), wordDict.end());
        //dp[i]=true表示s[0..i-1]能在wordDict找到对应的组合
        vector<bool> dp(s.size()+1, false);
        dp[0] = true;
        
        for(int i=1;i<=s.size();++i){
            for(int j=i-1;j>=0;--j){
                if(dp[j]){
                    string t = s.substr(j, i-j);
                    auto p = lower_bound(wordDict.begin(), wordDict.end(), t);
                    if(*p==t){
                        dp[i] = true;
                        break;
                    }
                }
            }
        }
        
        return dp[s.size()];
    }
};
