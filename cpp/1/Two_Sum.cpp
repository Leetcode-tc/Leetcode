class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        unordered_map<int, int> um;
        for(int i=0;i<nums.size();++i){
            if(um.find(nums[i])!=um.end()){
                ret.push_back(um[nums[i]]);
                ret.push_back(i);
            }
            else{
                um[target-nums[i]] = i;
            }
        }
        return ret;
    }
};