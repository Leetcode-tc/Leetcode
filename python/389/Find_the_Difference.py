class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        for c in t:
            # d[c] -= 1
            # if d[c] < 0:
            #     return c
            if c not in d or d[c] -1 < 0:
                return c
            d[c] -= 1
            