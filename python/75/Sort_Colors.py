class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)-1
        k = -1
        while i <= j:
            if nums[i] == 0:
                nums[k+1], nums[i] = nums[i], nums[k+1]
                i += 1
                k += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            
# 三路快排
# [0,1,0]
# i <= j
