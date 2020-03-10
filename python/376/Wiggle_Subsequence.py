class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        stack = [nums[0]]
        flag = None
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                if flag == 1:
                    stack.pop()
                stack.append(nums[i])
                flag = 1
            elif nums[i] < nums[i-1]:
                if flag == -1:
                    stack.pop()
                stack.append(nums[i])
                flag = -1
        return len(stack)