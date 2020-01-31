class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product, sum = 1, 0
        while n > 0:
            product *= (n%10)
            sum += (n%10)
            n /= 10
        return product -sum
        
