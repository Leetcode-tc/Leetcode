class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> vv(n, vector<int>(n, -1));
        return solve(nums, 0, n-1, vv)>=0;
    }
    
    int solve(vector<int> &nums, int i, int j, vector<vector<int>> &vv){
        if(vv[i][j]<0){
            vv[i][j] = (i==j?nums[i]:max(nums[i]-solve(nums, i+1, j, vv), nums[j]-solve(nums, i, j-1, vv)));
        }
        return vv[i][j];
    }
};
