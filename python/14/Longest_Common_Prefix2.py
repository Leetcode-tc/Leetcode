class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ''
        for item in zip(*strs):
            s = set(item)
            if len(s) == 1:
                ret += list(s)[0]
            else:
                break
        return ret
