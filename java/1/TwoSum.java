import java.util.HashMap;

/**
 * @author: create by nadao
 * @version: v1.0
 * @description: 两数之和
 * @date:2019/11/19
 */
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        if(nums.length == 0){
            return null;
        }
        int[] res = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int partnerKey = target-nums[i];
            if (map.containsKey(partnerKey)){
                res = new int[]{map.get(partnerKey), i};
            }
            map.put(nums[i],i);
        }
        return res;
    }
}
