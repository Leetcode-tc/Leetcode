class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int i = 0, j = 0;
        int currentSum = 0;
        int ret = 0;
        while(j<nums.size()){
            currentSum += nums[j++];
            while(currentSum>=s){
                if(ret==0||ret>j-i){
                    ret = j-i;
                }
                currentSum -= nums[i++];
            }
        }
        return ret;
    }
};
