class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        res = sys.maxint
        for i in range(n):
            left = i + 1
            right = n - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(res - target):
                    res = sum
                if sum < target:
                    left += 1
                else:
                    right -= 1
        return res