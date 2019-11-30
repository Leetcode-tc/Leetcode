class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        d = {}
        def dfs(target, index):
            if (target, index) in d:
                return d[(target,index)]
            if index == len(nums):
                if target == 0:
                    d[(target,index)] = 1
                else:
                    d[(target,index)] = 0
            else:
                d[(target,index)] = dfs(target+nums[index],index+1) + dfs(target-nums[index],index+1)
            return d[(target, index)]
        return dfs(S,0)
