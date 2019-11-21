/**
 * @author: create by nadao
 * @version: v1.0
 * @description: 搜索插入位置
 * @date:2019/11/19
 */
public class SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length-1;
        while(start+1 < end){
            int mid = (end-start)/2+start;
            if(nums[mid] == target) {
                return mid;
            }
            if(nums[mid] < target){
                start = mid;
            }else {
                end = mid;
            }
        }
        if (target <= nums[start]){
            return start;
        }else if (target <= nums[end]){
            return end;
        }else{
            return end+1;
        }
    }
}
