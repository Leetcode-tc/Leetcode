class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        a = 0
        b = 1
        for i in range(N):
            a, b = b, a+b
        return a
