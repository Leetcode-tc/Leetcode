class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-min(nums)*len(nums)             



# 超出时间限制
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        n = len(nums)
        maxIndex = 0
        for i in range(1, n):
            if nums[i] > nums[maxIndex]:
                maxIndex = i
        curSum = sum(nums)
        cnt = 0
        while nums[maxIndex] * n != curSum:
            curMaxIndex = maxIndex
            for i in range(n):
                if i != curMaxIndex:
                    nums[i] += 1
                if nums[i] > nums[maxIndex]:
                    maxIndex = i
            curSum += n-1
            cnt += 1
        return cnt