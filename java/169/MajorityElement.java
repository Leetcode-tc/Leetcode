class Solution {
    public int majorityElement(int[] nums) {


        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (map.containsKey(num)) {
                int count = map.get(num) + 1;
                if (count > nums.length / 2) {
                    return num;
                }
                map.put(num, count);
            } else {
                map.put(num, 1);
                if (nums.length == 1) {
                    return num;
                }
            }
        }
        throw new IllegalArgumentException("No solution!");
    }
}