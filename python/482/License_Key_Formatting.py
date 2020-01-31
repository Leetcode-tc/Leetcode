class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []
        cnt = 0
        for i in range(len(S)-1,-1,-1):
            if S[i] != '-':
                if cnt == K:
                    res.append('-')
                    cnt = 0
                res.append(S[i].upper())
                cnt += 1
                
        return ''.join(res[::-1])


# "5F3Z-2e-9-w"
# 4
# "--a-a-a-a--"
# 2