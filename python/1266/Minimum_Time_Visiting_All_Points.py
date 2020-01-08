class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 2 or len(points[0]) == 0:
            return 0
        cnt = 0
        for i in range(1,len(points)):
            dx = abs(points[i][0] - points[i-1][0])
            dy = abs(points[i][1] - points[i-1][1])
            if dx == dy:
                cnt += dx
            else:
                cnt += max(dx, dy)
        return cnt

