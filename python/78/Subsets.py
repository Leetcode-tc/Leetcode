class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for num in nums:
            output += [cur + [num] for cur in output]
        return output



    # 位运算
    def subsets2(self, nums):
        n = len(nums)
        # 2 ^ n
        size = 1 << n
        res = []
        for i in range(size):
            cur = []
            for j in range(n):
                if i & (1 << j):
                    cur.append(nums[j])
            res.append(cur)
        return res
