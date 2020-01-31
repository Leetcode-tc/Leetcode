class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squre = [i for i in range(1, n + 1) if int(math.sqrt(i)) ** 2 == i]
        q = []
        q.append((0, 0))
        duplicate = set()
        while q:
            cur, step = q.pop(0)
            step += 1
            for x in squre:
                x += cur
                if x == n:
                    return step
                if x < n and (x, step) not in duplicate:
                    duplicate.add((x, step))
                    q.append((x, step))
        return 0
