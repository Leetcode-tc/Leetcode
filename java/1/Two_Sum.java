public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> m = new HashMap<Integer,Integer>();
        int[] ret = new int[2];
        for(int i=0;i<nums.length;++i){
            if(m.get(nums[i])!=null){
                ret[0] = m.get(nums[i]);
                ret[1] = i;
                break;
            }
            else{
                m.put(target-nums[i],i);
            }
        }
        return ret;
    }
}