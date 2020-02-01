class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        s = {1,}
        i, j = 2, num-1
        while i <= j:
            j = num/i
            if num % i == 0:
                s.add(i)
                s.add(j)
            i += 1
        return sum(list(s)) == num
