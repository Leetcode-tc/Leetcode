class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.size()==0) return -1;
        int left = 0, right = nums.size()-1;
        while(left<=right){
            int mid = left+(right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            else if(nums[mid]<target){
                if(target<=nums[right]||nums[mid]>nums[right]){
                    left = mid+1;
                }
                else{
                    right = mid-1;
                }
            }
            else{
                if(target>=nums[left]||nums[mid]<nums[left]){
                    right = mid-1;
                }
                else{
                    left = mid+1;
                }
            }
        }
        return -1;
    }
};