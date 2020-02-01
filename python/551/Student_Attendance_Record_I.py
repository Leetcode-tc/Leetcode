class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cntA = 0
        cntL = 0
        for i in range(len(s)):
            if s[i] == 'A':
                cntA += 1
            elif s[i] == 'L':
                if i+2< len(s) and s[i+1] == s[i+2] =='L':
                    cntL += 1
                    break
        return cntA<=1 and cntL == 0