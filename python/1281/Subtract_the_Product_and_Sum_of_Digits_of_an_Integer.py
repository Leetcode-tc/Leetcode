class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product, sum = 1, 0
        for x in str(n):
            product *= int(x)
            sum += int(x)
        return product - sum
