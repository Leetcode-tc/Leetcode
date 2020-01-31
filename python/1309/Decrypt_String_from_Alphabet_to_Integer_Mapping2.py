class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = [str(i)+'#' if i>=10 else str(i) for i in range(1,27)]
        b = [chr(i) for i in range(97,123)]
        d = dict(zip(a,b))
        i = 0
        res =''
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                res += d[s[i:i+3]]
                i += 3
            else:
                res += d[s[i]]
                i += 1
        return res



