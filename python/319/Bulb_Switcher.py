class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        while res * res <= n:
            res += 1
        return res - 1
