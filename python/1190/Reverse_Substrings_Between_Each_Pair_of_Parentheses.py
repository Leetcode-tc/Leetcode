class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res =[]
        ret = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                res.append([stack[-1], i])
                stack.pop()
        for x in res:
            i, j = x[0]+1, x[1]-1
            ret[x[0]] = ret[x[1]] = ''
            while i < j:
                ret[i], ret[j] = ret[j], ret[i]
                i += 1
                j -= 1
        return ''.join(ret)
