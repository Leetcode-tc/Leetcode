class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a)-1, len(b)-1
        carry = 0
        res = ''
        while i>=0 or j>=0:
            n1 = int(a[i]) if i>=0 else 0
            i -= 1
            n2 = int(b[j]) if j>=0 else 0
            j -= 1
            num = n1 + n2 + carry
            res = str(num%2) + res
            carry = num/2
        return res if carry==0 else str(carry) + res
