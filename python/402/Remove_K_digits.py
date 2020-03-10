class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        finalstack = stack[:-k] if k > 0 else stack
        return ''.join(finalstack).lstrip('0') or "0"

        # num = "10" k=1 or k =2 从原数字移除所有的数字，剩余为空就是0
        # num = "10200" k = 1

