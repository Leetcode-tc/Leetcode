class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        ms = map(lambda x:int(x[:2])*60+int(x[3:]), timePoints)
        ms.sort()
        return min(map(lambda a,b:(b-a)%(24*60), ms, ms[1:]+ms[:1]))
