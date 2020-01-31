class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        carry = 1
        for i in range(n - 1, -1, -1):
            num = digits[i] + carry
            digits[i] = num % 10
            carry = num / 10
            if carry == 0:
                break
        if carry:
            digits.insert(0, carry)
        return digits
