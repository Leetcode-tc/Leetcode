class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        numToHex = [str(x) for x in range(10)] + [chr(x) for x in range(97,103)]
        res = []
        if num == -2**31:
            return '80000000'
        flag = False
        if num < 0:
            flag = True
            num = -num
        while num or len(res)<8:
            res.append(num%16)
            num /= 16
        if flag:
            for i,x in enumerate(res):
                res[i] = 15-x
            carry = 1
            i = 0
            while carry >0 :
                carry += res[i]
                if i < len(res):
                    res[i] = carry % 16
                else:
                    res.append(carry % 16)
                carry /= 16
                i += 1
        for i, x in enumerate(res):
            res[i] = numToHex[x]
        res = ''.join(reversed(res)).lstrip('0')
        return res if res != '' else '0'
