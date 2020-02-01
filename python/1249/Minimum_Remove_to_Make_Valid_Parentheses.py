class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                res.append('')
            elif s[i] == ')':
                if len(stack)>0:
                    res.append(s[i])
                    res[stack.pop()] = '('
                else:
                    res.append('')
            else:
                res.append(s[i])
        return ''.join(res)
