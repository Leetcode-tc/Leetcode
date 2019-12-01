class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        maxNum, preMaxNum = 0, -1
        for i in range(1, len(nums)):
            if nums[i] > nums[maxNum]:
                preMaxNum = maxNum
                maxNum = i
            elif preMaxNum == -1 or nums[i] > nums[preMaxNum]:
                preMaxNum = i
        if nums[maxNum] >= nums[preMaxNum]*2:
            return maxNum
        return -1
