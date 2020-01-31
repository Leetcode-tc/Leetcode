class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        i, j = 0, 0
        while i < len(t):
            while i < len(t) and t[i] != s[j]:
                i += 1
            i += 1
            j += 1
            if j == len(s) and i <= len(t):
                return True
        return False