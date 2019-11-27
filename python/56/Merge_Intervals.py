class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        n = len(intervals)
        ret = [intervals[0]]
        for i in range(1,n):
            if intervals[i][0] <= ret[-1][1]:
                right = max(ret[-1][1],intervals[i][1])
                ret[-1] = [ret[-1][0],right]
            else:
                ret.append(intervals[i])
        return ret