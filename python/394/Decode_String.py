class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        while '[' in s:
            s=re.sub(r"(\d+)\[(\w+)\]", lambda m:m.group(2)*int(m.group(1)), s)
        return s
