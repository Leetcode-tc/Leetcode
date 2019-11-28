class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0:
            return True
        if len(s) & 1: 
            return False

        stack = []
        m = {'}': '{', ')': '(', ']': '['}

        for c in s:
            if c in m.values():
                stack.append(c)
            elif c in m.keys():
                if len(stack) != 0 and m[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0
