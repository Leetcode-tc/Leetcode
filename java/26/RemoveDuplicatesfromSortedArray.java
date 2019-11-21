/**
 * @author: create by nadao
 * @version: v1.0
 * @description: 删除有序数组中重复的项
 * @date:2019/11/19
 */
public class RemoveDuplicatesfromSortedArray {
    public int removeDuplicates(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }
        int res = 1;
        for (int i = 1; i < nums.length; i++) {
            if(nums[i-1] != nums[i]){
                nums[res++] = nums[i];
            }
        }
        return res;
    }
}

