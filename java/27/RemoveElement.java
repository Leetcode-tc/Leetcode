/**
 * @author: create by nadao
 * @version: v1.0
 * @description: 移除元素
 * @date:2019/11/19
 */
public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        if (nums == null || nums.length == 0){
            return 0;
        }
        int res=0;
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] != val){
                nums[res++] = nums[i];
            }
        }
        return res;
    }
}
