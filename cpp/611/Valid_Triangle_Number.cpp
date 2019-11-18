class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int i = 0, j = 1;
        int ret = 0;
        
        for(i=0;i<nums.size();++i){
            for(j=i+1;j<nums.size();++j){
                auto pos = lower_bound(nums.begin()+j+1, nums.end(), nums[i]+nums[j]);
                ret += pos-(nums.begin()+j+1);
            }
        }
        
        return ret;
    }
};
