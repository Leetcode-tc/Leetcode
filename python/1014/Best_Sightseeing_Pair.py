class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        pre_max = A[0] + 0
        for j in range(1, len(A)):
            res = max(res, pre_max+A[j]-j)
            pre_max = max(pre_max, A[j]+j)
        return res
        
# (A[i] + i) + (A[j] - j)
        
