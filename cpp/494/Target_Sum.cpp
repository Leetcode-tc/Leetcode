class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        /*假设T(i, n, t)表示数组nums[i..n]中的数的值组成t的方案数，
        因为nums[i]的符号有+，-两种选择，所以T(i, n, t)有如下关系式：
                T(i, n, t) = T(i+1, n, t-nums[i]) + T(i+1, n, t+nums[i])
        其中，nums[i]的符号分别为+和-*/
        if(nums.size()==0) return 0;
        return subsetNum(nums, S);
        return solve(nums, 0, S);
    }
    
    int solve(vector<int> &nums, int i, int target){
        if(i==nums.size()-1){
            return (target==0&&nums[i]==0)?2:abs(nums[i])==abs(target)?1:0;
        }
        return solve(nums, i+1, target-nums[i]) + solve(nums, i+1, target+nums[i]);
    }
    
    //题解里有一种非常聪明的解法：
    //令S(P),S(N)分别为符号为+，-的子集的和，则有如下关系：
    //          S(P) + S(N) = sum(nums)
    //          S(P) - S(N) = target
    //S(P) + S(N) + S(P)- S(N) = sum(nums) + target
    //          S(P) = (sum + target) / 2
    //所以只需求nums中和为(sum+target)/2的子集个数，且sum+target为奇数时子集为0
    int subsetNum(vector<int> &nums, int S){
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int target = sum + S;
        if(target&0x1==1||sum<S) return 0;
        target /= 2;
        vector<int> dp(target+1,0);
        dp[0] = 1;
        for(int i=0;i<nums.size();++i){
            for(int j=target;j>=nums[i];--j){
                dp[j] += dp[j-nums[i]];
            }
        }
        return dp[target];
    }
};
