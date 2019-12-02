
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        for i in range(len(haystack)-len(needle)+1):
            j = 0
            if haystack[i] == needle[0]:
                k = i
                while j < len(needle) and haystack[k] == needle[j]:
                    k += 1
                    j += 1
                if j == len(needle):
                    return i
        return -1
