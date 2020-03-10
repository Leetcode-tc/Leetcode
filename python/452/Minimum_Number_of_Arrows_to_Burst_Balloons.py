class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        points.sort(key=lambda x:x[1])
        arrows = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            if x_start > first_end:
                arrows += 1
                first_end = x_end
        return arrows