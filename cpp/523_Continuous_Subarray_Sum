class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(nums.begin(), nums.end());
        for(int i=2;i<=n;++i){
            for(int j=n-1;j>=i-1;--j){
                dp[j] = dp[j-1]+nums[j];
                if(k==0&&dp[j]==0)
                    return true;
                if(k&&dp[j]%k==0)
                    return true;
            }
        }
        return false;
    }
    
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_set<int> us;
        int sum = 0;
        if(k==0){
            for(int i=0;i<nums.size()-1;++i){
                if(nums[i]==0&&nums[i+1]==0)
                    return true;
            }
            return false;
        }
        if(k<0)
            k = -k;
        for(int i=0;i<nums.size();++i){
            sum += nums[i];
            sum %= k;
            if(us.find(sum)!=us.end()||(i>0&&sum==0)){
                return true;
            }
            us.insert(sum);
        }
        return false;
    }
};
