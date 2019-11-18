class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 1;
        int currentNum = nums[0];
        for(int i=1;i<nums.size();++i){
            if(count<=0){
                count = 1;
                currentNum = nums[i];
            }
            else if(currentNum==nums[i]){
                count++;
            }
            else{
                count--;
            }
        }
        return currentNum;
    }
};
