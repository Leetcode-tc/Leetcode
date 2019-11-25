class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # 右边有序or右边乱序
                if target <= nums[right] or nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # 左边有序or左边乱序
                if target >= nums[left] or nums[mid] < nums[left]:
                    right = mid -1
                else:
                    left = mid + 1
        return -1
