class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if(sum&0x1) return false;
        int target = sum>>1;
        vector<bool> dp(target+1, false);
        dp[0] = true;
        for(int n:nums){
            for(int i=target;i>=n;--i){
                dp[i] = dp[i]||dp[i-n];
            }
        }
        return dp[target];
    }
};
