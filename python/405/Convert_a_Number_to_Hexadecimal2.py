class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        for i in range(8):
            res = '0123456789abcdef'[num&15] + res
            num >>= 4
        res = res.lstrip('0')
        return '0' if res == '' else res