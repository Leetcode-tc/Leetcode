class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for x in tokens:
            if not x in "+-*/":
                stack.append(int(x))
            else:
                first = stack.pop()
                second = stack.pop()
                res = int(eval(str(second * 1.0) + x + str(first)))
                stack.append(res)
        return stack[-1]

# 6 / -132 = -1
# int(6.0 / -132) = 0
