class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for x in s:
            if len(stack) == 0 or stack[-1][0] != x:
                stack.append([x,1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        return ''.join([x[0]*x[1] for x in stack])