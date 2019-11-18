class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        :description: 用set可以自动去重，由于set不能用list，所以用tuple来操作，最后转为list
                      对于nums[0..i]的解，其实就是nums[0..i-1]的解集合和加入nums[i]后新的解集合
                      的union，比如对于[4,6,7,7],nums[0..2]的解集合为
                          Set1:{(4,6),(4,7),(6,7),(4,6,7)}
                      加入7之后，7和nums[0..2]中小于等于7的数可以组成新的解，7和nums[0..2]的解集
                      合也可以组成新的解，因此新的集合为
                          Set2:{(4,7),(6,7),(7,7),(4,6,7),(4,6,7,7),(4,7,7),(6,7,7)}
                      最后的结果就是union(Set1,Set2)
        """
        ret = set()
        for i in xrange(len(nums)):
            ret.update([tuple(list(x)+[nums[i]]) for x in ret if nums[i]>=x[-1]])
            ret.update([(n, nums[i]) for n in nums[:i] if nums[i]>=n])
        return map(list, ret)
