ass Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                left += 1
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # while left < right and nums[left] == nums[left-1]:
                    #     left += 1
                    # while left < right and nums[right] == nums[right+1]:
                    #     right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        # return res
        return [list(t) for t in set([tuple(t) for t in res])]

# 二维列表，必须先把列表中每个元素转化为tuple，list不可哈希但是tuple可哈希。
# TypeError: unhashable type: 'list'
