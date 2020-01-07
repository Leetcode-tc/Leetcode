class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for x in nums:
            tmp = 0
            while x:
                tmp += 1
                x /= 10
            if tmp & 1 == 0:
                cnt += 1
        return cnt    
