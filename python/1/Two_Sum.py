class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if dict.has_key(nums[i]):
                return [dict[nums[i]],i]
            else:
                dict[target-nums[i]] = i