class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = sorted([(i,x) for i,x in enumerate(nums)], key=lambda x:x[1], reverse=True)
        names = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4,len(nums)+1))
        ranks = ['' for _ in range(len(nums))]
        for i in range(len(res)):
            ranks[res[i][0]] = names[i]
        return ranks
                