class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        ls = 0
        for i in range(len(nums)):
            if ls *2 + nums[i] == s:
                return i
            ls += nums[i]
        return -1
