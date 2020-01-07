class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        mid = n/2
        res = [x for x in range(-mid, mid+1)]
        if n & 1 == 0:
            res.remove(0)
        return res
        
