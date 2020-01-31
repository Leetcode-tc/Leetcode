class Solution {
    public int firstMissingPositive(int[] nums) {
        // 检测1是否存在，如果不存在，那么要找的整数就是1
        int contains = 0;
        for (int num : nums) {
            if (num == 1) {
                contains = 1;
                break;
            }
        }
        if (contains == 0) {
            return 1;
        }

        // 用1替换：1）负数；2）0；3）大于n的数
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] <= 0 || nums[i] > n) {
                nums[i] = 1;
            }
        }

        // 对于nums[i]为n的索引，使用nums[0]的正负值表示；
        // 对于nums[i]为其他值的索引，使用nums[nums[i]]的正负值表示
        for (int i = 0; i < n; i++) {
            int index = Math.abs(nums[i]);
            if (index == n) {
                nums[0] = - Math.abs(nums[0]);
            } else {
                nums[index] = - Math.abs(nums[index]);
            }
        }

        for (int i = 1; i < n; i++) {
            if (nums[i] > 0) {
                return i;
            }
        }
        if (nums[0] > 0) {
            return n;
        }
        // 如果1到n左右的元素都存在，那么缺少的就是n+1
        return n + 1;
    }
}