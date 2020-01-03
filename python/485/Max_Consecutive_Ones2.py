class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        cnt = 0
        for x in nums:
            if x == 1:
                cnt += 1
            else:
                cnt = 0
            ret = max(cnt, ret)
        return ret
