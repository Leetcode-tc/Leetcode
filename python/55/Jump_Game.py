class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxlen = 0
        for i, jump in enumerate(nums):
            if maxlen >= i and i + jump > maxlen:
                maxlen = i+jump
        return maxlen >= len(nums)-1


    def canJump2(self, nums):
        maxlen = 0
        for i in range(len(nums)):
            if i > maxlen:
                return False
            maxlen = max(maxlen, i+nums[i])
        return True
