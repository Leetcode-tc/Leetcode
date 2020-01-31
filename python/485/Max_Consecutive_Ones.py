class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ret = 0
        i = 0
        while i < n:
            if nums[i] == 1:
                j = i
                j += 1
                while j < n and nums[j] == nums[i]:
                    j += 1
                ret = j-i if j-i > ret else ret
                i = j
            else:
                i += 1
        return ret
