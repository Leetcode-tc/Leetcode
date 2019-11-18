class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)):
            res += d[s[i]]
            if i > 0 and d[s[i-1]] < d[s[i]]:
                res -= 2*d[s[i-1]]
        return res
