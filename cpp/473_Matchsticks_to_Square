class Solution {
public:
    bool makesquare(vector<int> &nums){
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if(sum%4!=0||nums.size()<4) return false;
        sort(nums.begin(), nums.end(), [](int a, int b){return a>b;});
        int target = sum/4;
        if(nums[0]>target) return false;
        int k = 4, i;
        for(i=0;i<nums.size()&&nums[i]==target;++i)
            k--;
        vector<int> A(k,0);
        return solve(nums, A, i, target);
    }
    //对于nums数组中的每一个数，有4种去处，分别遍历
    bool solve(vector<int> &nums, vector<int>& A, int i, int target){
        if(i==nums.size()){
            return all_of(A.begin(), A.end(), [target](int t){return t==target;});
        }
        for(int j=0;j<A.size();++j){
            if(A[j]+nums[i]>target)
                continue;
            bool needSkip = false;
            for(int k=0;k<j;++k){
                if(A[k]==A[j]){
                    needSkip = true;
                    break;
                }
            }
            if(needSkip) continue;
            A[j] += nums[i];
            if(solve(nums, A, i+1, target))
                return true;
            A[j] -= nums[i];
        }
        return false;
    }
};
